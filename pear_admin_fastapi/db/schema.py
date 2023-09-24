from datetime import datetime

from pydantic import BaseModel as PydanticBaseModel, ConfigDict


class BaseModel(PydanticBaseModel):
    model_config = ConfigDict(from_attributes=True)


class BaseIntegerID(BaseModel):
    id: int


class BaseCreateTime(BaseModel):
    created_at: datetime


class BaseUpdateTime(BaseModel):
    created_at: datetime


class BaseDeleteTime(BaseModel):
    created_at: datetime


class BaseCUDTime(BaseCreateTime, BaseUpdateTime, BaseDeleteTime):
    pass
