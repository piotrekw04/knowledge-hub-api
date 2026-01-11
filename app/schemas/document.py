from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class DocumentCreate(BaseModel):
    filename: str
    content: str


class DocumentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    filename: str
    content: str
    created_at: datetime


class DocumentUpdate(BaseModel):
    filename: str | None = None
    content: str | None = None
