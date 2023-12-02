from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.utils.dependencies import get_pagination
from app.database import get_db

from . import router, schemas, models as m


@router.get('/', response_model=list[schemas.CustomerOut], dependencies=[Depends(get_current_user)])
async def read_customers(pagination: dict = Depends(get_pagination), db: Session = Depends(get_db)):
    return db.query(m.Customer).order_by(
        m.Customer.id.desc()
    ).offset(
        pagination['offset']
    ).limit(
        pagination['limit']
    ).all()


@router.post('/', response_model=schemas.CustomerOut, status_code=201, dependencies=[Depends(get_current_user)])
async def add_customer(customer_data: schemas.CustomerCreate, db: Session = Depends(get_db)):
    customer = m.Customer(**customer_data.model_dump())
    customer.save(db)
    return customer


@router.get('/{customer_id}', response_model=schemas.CustomerOut, dependencies=[Depends(get_current_user)])
async def read_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(m.Customer).filter_by(id=customer_id).first()
    if customer is None:
        raise HTTPException(status_code=404, detail='Customer not found')
    return customer
