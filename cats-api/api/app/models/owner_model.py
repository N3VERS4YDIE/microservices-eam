from pydantic import BaseModel, EmailStr, Field, field_validator


class OwnerModel(BaseModel):
    id: int = Field(...)
    cat_ids: list[int]
    name: str
    email: EmailStr = Field(...)
    password: str = Field(..., min_length=2)

    @field_validator("password")
    def validate_password(cls, v):
        if not any(char.isdigit() for char in v):
            raise ValueError("Password must contain at least one number")
        if not any(char.isalpha() for char in v):
            raise ValueError("Password must contain at least one letter")
        return v

    class Config:
        orm_mode = True
