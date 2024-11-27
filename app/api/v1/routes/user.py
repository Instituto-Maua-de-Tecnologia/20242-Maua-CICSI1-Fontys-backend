from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import CreateUserSchema, UserResponseSchema
from app.services.user_service import UserService
from app.controllers.user_controller import CreateUserController
from app.core.database import get_db


router = APIRouter()

def get_create_user_controller(db: Session = Depends(get_db)) -> CreateUserController: # type: ignore
    service = UserService(db)
    return CreateUserController(service)

@router.post("/users", response_model=UserResponseSchema, status_code=201)
def create_user(
    data: CreateUserSchema,
    controller: CreateUserController = Depends(get_create_user_controller)
) -> UserResponseSchema:
    return controller.handle(data)

@router.get('/health', response_model=dict)
def health() -> dict:
    return {'status': 'ok', 'uptime': 'running'}
