from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.user import UserCreate, User
from app.services.user_service import UserService

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
def login_route():
    return UserService.login()

@router.get("/auth/callback")
async def auth_callback_route(code: str, db: Session = Depends(get_db)):
    return await UserService.auth_callback(code, db)



