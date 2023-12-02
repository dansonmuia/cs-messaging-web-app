from fastapi import FastAPI

from app import auth, users, customers

# Import Base here for discovery by alembic
from app.database import Base

app = FastAPI()

app.include_router(auth.router, tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(customers.router, prefix="/customers", tags=["Customers"])
