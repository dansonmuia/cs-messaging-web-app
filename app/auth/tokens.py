import os
from datetime import datetime, timezone, timedelta
import jwt

from app.users.models import User


ACCESS_TOKEN_EXPIRY = 60*60*6  # 6 hrs

JWT_ALGORITHM = "HS256"

SECRET_KEY = os.getenv('SECRET_KEY')


def generate_access_token(user: User):
    return jwt.encode(
        {
            "exp": datetime.now(tz=timezone.utc) + timedelta(seconds=ACCESS_TOKEN_EXPIRY),
            'email': user.email
        },
        SECRET_KEY,
        algorithm=JWT_ALGORITHM
    )


def load_user_from_access_token(token, db):
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=[JWT_ALGORITHM])
        email = data.get('email')
        return db.query(User).filter_by(email=email).first()
    except Exception:
        return None
