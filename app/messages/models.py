from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, Text, Boolean

from app.database import Base
from app.utils.db import DbSaveMixin


class CustomerMessage(Base, DbSaveMixin):
    __tablename__ = 'customer_messages'

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    body = Column(Text())
    response = Column(Text())
    is_urgent = Column(Integer, default=0)
    assigned_to = Column(Integer, ForeignKey('users.id'), index=True)
    is_closed = Column(Boolean(), default=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
