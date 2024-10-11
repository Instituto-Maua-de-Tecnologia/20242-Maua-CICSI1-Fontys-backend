from fastapi import APIRouter
from app.db.session import SessionLocal


router = APIRouter()

import os

def get_db():
    print("SQLALCHEMY", os.environ.get("DATABASE_URL"))
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        



