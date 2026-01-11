from fastapi import APIRouter, Depends, status
from app.db.session import get_db
from app.schemas.document import DocumentCreate, DocumentResponse
from app.services.document_service import create_document
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=DocumentResponse)
async def add_document(
    document_data: DocumentCreate, db: AsyncSession = Depends(get_db)
):
    document = await create_document(db=db, document_in=document_data)
    return document
