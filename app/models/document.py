import uuid
from datetime import datetime
from app.db.base import Base
from sqlalchemy import Text, String, DateTime, UUID
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func


class Document(Base):
    __tablename__ = "documents"

    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    filename: Mapped[str] = mapped_column(String(255))
    content: Mapped[str] = mapped_column(Text())
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
