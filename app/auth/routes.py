from sqlalchemy.orm import Session

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app.database import get_db
from app.users.models import User

from . import router, schemas
from .tokens import generate_access_token


def get_user_token(email: str, password: str, db: Session):
    user = db.query(User).filter_by(email=email).first()
    if user and user.is_active and user.check_password(password):
        return {
            "access_token": generate_access_token(user),
            "token_type": "bearer",
            "expires_in": "6h",
            "user": {
                "id": user.id,
                "name": user.name,
                "email": user.email,
            }
        }
    raise HTTPException(status_code=400, detail='Invalid credentials')


@router.post('/login-for-token')
async def login(credentials: schemas.AuthSchema, db: Session = Depends(get_db)):
    return get_user_token(credentials.email, credentials.password, db)


# For logging in while on the swagger docs
@router.post('/docs-login-here')
async def login_from_docs(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return get_user_token(form_data.username, form_data.password, db)
