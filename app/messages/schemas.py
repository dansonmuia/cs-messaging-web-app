from datetime import datetime

from pydantic import BaseModel, Field


class MessageBase(BaseModel):
    customer_id: int
    body: str
    is_urgent: int = Field(0, ge=0, le=1)


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
