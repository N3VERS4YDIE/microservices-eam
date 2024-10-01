from datetime import datetime

from pydantic import BaseModel, Field


class CatModel(BaseModel):
    id: int = Field(...)
    owner_ids: list[int]
    name: str
    birthdate: datetime
    description: str = Field(..., max_length=500)

    class Config:
        orm_mode = True
