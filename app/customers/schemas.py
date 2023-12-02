from datetime import datetime

from pydantic import BaseModel, Field


class CustomerBase(BaseModel):
    name: str | None = Field(None, min_length=2, max_length=32)
    phone: str | None = Field(None, min_length=10, max_length=16)
    address: str | None = Field(None, max_length=256)
    loan_limit: int | None


class CustomerCreate(CustomerBase):
    ...


class CustomerOut(CustomerBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

