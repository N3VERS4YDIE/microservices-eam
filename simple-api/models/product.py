from models.base import BaseModel

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    created_at: str
    updated_at: str