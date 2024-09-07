from models.base import BaseModel

class User(BaseModel):
    email: str
    password: str