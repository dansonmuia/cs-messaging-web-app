from datetime import datetime

from pydantic import BaseModel


class MessageBase(BaseModel):
    customer_id: int
    body: str
    is_urgent: bool = False


class MessageCreate(MessageBase):
    ...


class MessageResponse(BaseModel):
    response: str


class MessageOut(MessageBase, MessageResponse):
    id: int
    assigned_to: int | None = None
    is_closed: bool
    created_at: datetime

    class Config:
        from_attributes = True
