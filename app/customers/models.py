from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from app.database import Base
from app.utils.db import DbSaveMixin


class Customer(Base, DbSaveMixin):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(32))
    phone = Column(String(16), index=True)
    address = Column(String(256))
    # Loan limit in KSH
    loan_limit = Column(Integer, default=500)
    created_at = Column(DateTime, default=datetime.utcnow)
