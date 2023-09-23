from sqlalchemy.orm import DeclarativeBase

from pear_admin_fastapi.db.meta import meta


class Base(DeclarativeBase):
    """Base for all models."""

    metadata = meta
