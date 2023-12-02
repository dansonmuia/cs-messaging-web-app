from sqlalchemy import desc
from sqlalchemy.orm import Session

from fastapi import Depends, HTTPException

from app.database import get_db
from app.utils.dependencies import get_pagination
from app.auth.dependencies import get_current_user

from . import router, models as m, schemas


@router.get('/', response_model=list[schemas.UserOut], dependencies=[Depends(get_current_user)])
async def read_users(db: Session = Depends(get_db), pagination: dict = Depends(get_pagination)):
    return db.query(m.User).order_by(
        desc(m.User.id)
    ).offset(
        pagination['offset']
    ).limit(
        pagination['limit']
    ).all()


@router.post('/', response_model=schemas.UserOut, status_code=201, dependencies=[Depends(get_current_user)])
async def add_user(user_data: schemas.UserCreate, db: Session = Depends(get_db)):
    if db.query(m.User).filter_by(email=user_data.email).first():
        raise HTTPException(status_code=400, detail='This email is not available')

    user = m.User(**user_data.model_dump())
    user.save(db)
    return user
