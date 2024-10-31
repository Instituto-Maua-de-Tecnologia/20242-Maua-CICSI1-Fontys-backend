from fastapi import APIRouter
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.controlers.user_controler import create_user_controller
from app.schemas.user import CreateUserRequest, CreateUserResponse
from app.db.session import get_db


router = APIRouter()

@router.post("/user", response_model=CreateUserResponse)
async def create_user_endpoint(request: CreateUserRequest, db: Session = Depends(get_db)):
    return create_user_controller(request.email, request.name, request.password, db)





