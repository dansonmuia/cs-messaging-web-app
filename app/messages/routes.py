from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.utils.dependencies import get_pagination
from app.customers.models import Customer
from app.database import get_db

from . import router, schemas, models as m


@router.get('/', response_model=list[schemas.MessageOut], dependencies=[Depends(get_current_user)])
async def read_messages(pagination: dict = Depends(get_pagination), db: Session = Depends(get_db)):
    return db.query(m.CustomerMessage).order_by(
        m.CustomerMessage.id.desc()
    ).offset(
        pagination['offset']
    ).limit(
        pagination['limit']
    ).all()


@router.post('/', response_model=schemas.MessageOut, status_code=201)
async def add_message(message_data: schemas.MessageCreate, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter_by(id=message_data.customer_id).first()
    if customer is None:
        raise HTTPException(status_code=400, detail='Customer with given ID not found')
    message = m.CustomerMessage(**message_data.model_dump())
    message.save(db)
    return message


@router.get('/{message_id}', response_model=schemas.MessageOut, dependencies=[Depends(get_current_user)])
async def read_message(message_id: int, db: Session = Depends(get_db)):
    message = db.query(m.CustomerMessage).filter_by(id=message_id).first()
    if message is None:
        raise HTTPException(status_code=404, detail='Message not found')
    return message


@router.put('/{message_id}', response_model=schemas.MessageOut, dependencies=[Depends(get_current_user)])
async def respond_to_message(message_id: int, message_data: schemas.MessageResponse, db: Session = Depends(get_db)):
    message = db.query(m.CustomerMessage).filter_by(id=message_id).first()
    if message is None:
        raise HTTPException(status_code=404, detail='Message not found')

    message.response = message_data.response
    message.is_closed = True
    message.save(db)
    return message


# Fetch messages assigned to current agent
@router.get('/assign-me', response_model=list[schemas.MessageOut])
async def read_assigned_messages(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return db.query(m.CustomerMessage).filter_by(
        assigned_to=current_user.id, is_closed=False
    ).all()


# Claim messages to handle
@router.post('/assign-me', response_model=list[schemas.MessageOut])
async def assign_me_messages(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    messages = db.query(m.CustomerMessage).filter_by(assigned_to=None, is_closed=False).limit(10).all()
    for message in messages:
        message.assigned_to = current_user.id
    db.add_all(messages)
    db.commit()
    return messages
