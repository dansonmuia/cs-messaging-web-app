from datetime import datetime

from pydantic import BaseModel, Field, EmailStr


class UserBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=32)
    email: EmailStr = Field(...)


class UserCreate(UserBase):
    password: str = Field(..., min_length=4, max_length=20)


class UserOut(UserBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True
