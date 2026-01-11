from app.schemas.document import DocumentCreate
from app.models.document import Document
from sqlalchemy.ext.asyncio import AsyncSession


async def create_document(db: AsyncSession, document_in: DocumentCreate) -> Document:
    document = Document(**document_in.model_dump())

    db.add(document)
    await db.commit()
    await db.refresh(document)

    return document
