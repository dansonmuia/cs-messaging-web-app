import os
import csv
from datetime import datetime

from app.database import get_db_context
from app.messages.models import CustomerMessage
from app.customers.models import Customer
from app.users.models import User


def seed_messages():
    try:
        with open('GeneralistRails_Project_MessageData_1.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                customer_id = row['User ID']
                timestamp = row['Timestamp (UTC)']
                body = row['Message Body']

                with get_db_context() as db:
                    customer = db.query(Customer).filter_by(id=customer_id).first()
                    if customer is None:
                        customer = Customer(id=customer_id)
                        db.add(customer)

                    date, time = timestamp.split(' ')
                    year, month, day = date.split('-')
                    hour, minute, second = time.split(':')
                    created_at = datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))

                    message = CustomerMessage(customer_id=customer_id, body=body, created_at=created_at)
                    db.add(message)
                    db.commit()

                    print(f'Added message {message.id} for customer {customer.id}')

    except FileNotFoundError:
        print('Seed questions file not found')


def create_admin(db):
    email = os.getenv('ADMIN_EMAIL')
    user = db.query(User).filter_by(email=email).first()
    if user is None:
        user = User(
            name=os.getenv('ADMIN_NAME'),
            password=os.getenv('ADMIN_PASSWORD'),
            email=email
        )
        user.save(db)
    return user


if __name__ == '__main__':
    with get_db_context() as db:
        create_admin(db)
    print('Admin created')

    seed_messages()
    print('Messages seeded')
