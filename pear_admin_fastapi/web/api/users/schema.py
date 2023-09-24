from typing import Optional, Any, List

from pydantic import BaseModel, Field, field_validator
from pear_admin_fastapi.db.schema import BaseIntegerID, BaseCUDTime


class BaseUser(BaseModel):
    username: str = Field(max_length=32)
    avatar: Optional[str] = Field(None, max_length=320)
    email: Optional[str] = Field(None, max_length=320)


class UserCreate(BaseUser):
    password: str = Field(max_length=128)


class UserRead(BaseIntegerID, BaseUser, BaseCUDTime):
    # roles: Optional[List[Any]] = None
    pass


class UserUpdate(BaseIntegerID):
    username: Optional[str] = Field(max_length=32)
    password: Optional[str] = Field(max_length=128)
    avatar: Optional[str] = Field(max_length=320)
    email: Optional[str] = Field(max_length=320)
