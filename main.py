from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import auth, users, customers, messages

# Import Base here for discovery by alembic
from app.database import Base

allowed_origins = ["http://localhost:3000", "http://127.0.0.1:3000", "https://branch.myduka.online"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth.router, tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(customers.router, prefix="/customers", tags=["Customers"])
app.include_router(messages.router, prefix="/messages", tags=["Customer Messages"])
