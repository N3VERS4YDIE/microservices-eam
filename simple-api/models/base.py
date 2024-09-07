from pydantic import BaseModel
from datetime import datetime

class BaseModel(BaseModel):
    id: int
    created_at: str
    updated_at: str
