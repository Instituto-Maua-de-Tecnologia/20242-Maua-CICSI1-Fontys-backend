from fastapi import APIRouter
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import User
from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository
from app.db.session import get_db


router = APIRouter()

@router.post("", response_model=User)
def create_user(user: User, db: Session = Depends(get_db)):
    user_service = UserService(UserRepository(db))
    new_user = user_service.create_user(db, user)
    return new_user




