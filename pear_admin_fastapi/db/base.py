from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from sqlalchemy import DateTime, Integer, func, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from pear_admin_fastapi.db.meta import meta


class Base(DeclarativeBase):
    """Base for all models."""
    __tablename__: str = None
    metadata = meta


class IntegerIDMixin(Base):
    __abstract__ = True
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)


class CreateTimeMixin(Base):
    __abstract__ = True

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())


class UpdateTimeMixin(Base):
    __abstract__ = True

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        onupdate=func.now(),
        server_default=func.now()
    )


class DeleteTimeMixin(Base):
    __abstract__ = True

    deleted_at: Mapped[Optional[datetime]] = mapped_column(DateTime, default=None)


class CUDTimeMixin(CreateTimeMixin, UpdateTimeMixin, DeleteTimeMixin):
    """Create, Update, Delete Time Mixin"""
    __abstract__ = True


class EnabledColumnMixin(Base):
    __abstract__ = True
    is_enabled: Mapped[bool] = mapped_column(Boolean, default=True)


