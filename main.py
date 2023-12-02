from fastapi import FastAPI


# Import Base here for discovery by alembic
from app.database import Base

app = FastAPI()
