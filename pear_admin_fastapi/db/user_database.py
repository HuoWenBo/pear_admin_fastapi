from typing import Optional, Generic

from fastapi_users.db.base import BaseUserDatabase
from fastapi_users.models import ID, UP
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase as BaseSQLAlchemyUserDatabase
from sqlalchemy import select, func


class UserDatabase(Generic[UP, ID], BaseUserDatabase[UP, ID]):
    """Base adapter for retrieving, creating and updating users from a database."""

    async def get_by_username(self, username: str) -> Optional[UP]:
        """Get a single user by username."""
        raise NotImplementedError()


class SQLAlchemyUserDatabase(Generic[UP, ID], BaseSQLAlchemyUserDatabase[UP, ID], UserDatabase[UP, ID]):
    async def get_by_username(self, username: str) -> Optional[UP]:
        statement = select(self.user_table).where(
            func.lower(self.user_table.username) == func.lower(username)
        )
        return await self._get_user(statement)
