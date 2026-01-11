from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.document import DocumentCreate, DocumentResponse, DocumentUpdate
from app.services.document_service import (
    create_document,
    delete_document,
    get_document,
    update_document,
)

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=DocumentResponse)
async def add_document(document_data: DocumentCreate, db: AsyncSession = Depends(get_db)):
    document = await create_document(db=db, document_in=document_data)
    return document


@router.get("/{document_id}", status_code=status.HTTP_200_OK, response_model=DocumentResponse)
async def read_document(document_id: UUID, db: AsyncSession = Depends(get_db)):
    document = await get_document(db=db, document_id=document_id)

    if document:
        return document
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.delete("/{document_id}", status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def erase_document(document_id: UUID, db: AsyncSession = Depends(get_db)):
    result = await delete_document(db=db, document_id=document_id)

    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return


@router.patch("/{document_id}", status_code=status.HTTP_200_OK, response_model=DocumentResponse)
async def patch_document(
    document_id: UUID, document_data: DocumentUpdate, db: AsyncSession = Depends(get_db)
):
    document = await update_document(db=db, document_id=document_id, document_in=document_data)

    if document:
        return document
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
