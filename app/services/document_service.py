from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.document import Document
from app.schemas.document import DocumentCreate, DocumentUpdate


async def create_document(db: AsyncSession, document_in: DocumentCreate) -> Document:
    document = Document(**document_in.model_dump())

    db.add(document)
    await db.commit()
    await db.refresh(document)

    return document


async def get_document(db: AsyncSession, document_id: UUID) -> Document | None:
    query = select(Document).where(Document.id == document_id)
    result = await db.scalar(query)

    return result


async def delete_document(db: AsyncSession, document_id: UUID) -> None | bool:
    result = await get_document(db=db, document_id=document_id)

    if result:
        await db.delete(result)
        await db.commit()
        return True
    else:
        return


async def update_document(
    db: AsyncSession, document_id: UUID, document_in: DocumentUpdate
) -> Document | None:
    result = await get_document(db=db, document_id=document_id)

    if result:
        document = document_in.model_dump(exclude_unset=True)

        for key, value in document.items():
            setattr(result, key, value)

        db.add(result)
        await db.commit()
        await db.refresh(result)

        return result
    else:
        return
