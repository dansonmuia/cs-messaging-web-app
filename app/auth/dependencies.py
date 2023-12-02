from sqlalchemy.orm import Session

from fastapi import Depends, HTTPException

from app.database import get_db
from app.users.models import User


from . import oauth2_scheme
from .tokens import load_user_from_access_token


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    user = load_user_from_access_token(token, db)
    if user is None:
        raise HTTPException(status_code=401, detail="You're not logged in")
    return user
