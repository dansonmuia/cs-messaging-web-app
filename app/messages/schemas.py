from datetime import datetime

from pydantic import BaseModel, Field

from app.users.schemas import UserOut
from app.customers.schemas import CustomerOut


class MessageBase(BaseModel):
    customer_id: int
    body: str
    is_urgent: int = Field(0, ge=0, le=1)


class MessageCreate(MessageBase):
    ...


class MessageResponse(BaseModel):
    response: str


class MessageOut(MessageBase):
    id: int
    response: str | None
    assigned_to: int | None = None
    assigned_to_user: UserOut | None
    customer: CustomerOut | None
    is_closed: bool
    created_at: datetime

    class Config:
        from_attributes = True
