from datetime import datetime

import bcrypt
from sqlalchemy import Column, String, DateTime, Integer

from app.database import Base
from app.utils.db import DbSaveMixin


class User(DbSaveMixin, Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(32), nullable=False)
    email = Column(String(64), nullable=False, unique=True, index=True)
    password_hash = Column(String(256))
    is_active = Column(String(16), default=True)
    created_at = Column(DateTime(), default=datetime.utcnow, index=True)

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, raw_password: str):
        hashed_password = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt())
        self.password_hash = hashed_password.decode('utf-8')

    def check_password(self, password) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))
