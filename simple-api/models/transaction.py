from models.base import BaseModel

class Transaction(BaseModel):
    amount: float
    description: str