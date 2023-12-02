from sqlalchemy import Column, Integer, String

from app.database import Base
from app.utils.db import DbSaveMixin


class Customer(Base, DbSaveMixin):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(32))
    phone = Column(String(16), index=True)
    address = Column(String(256))
