from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from app.controllers.get_all_users.get_all_users_controller import GetAllUsersController
from app.core.database import get_db
from app.schemas.user import CreateUserSchema, UserResponseSchema
from app.services.create_user.create_user_service import CreateUserService
from app.controllers.create_user.create_user_controller import CreateUserController
from app.services.get_all_users.get_all_users_service import GetAllUsersService


router = APIRouter()

def get_create_user_controller(db: Session = Depends(get_db)) -> CreateUserController:
    service = CreateUserService(db)
    return CreateUserController(service)


def get_get_all_users_controller(db: Session = Depends(get_db)) -> GetAllUsersController:
    service = GetAllUsersService(db)
    return GetAllUsersController(service)


@router.post("/users", response_model=UserResponseSchema, status_code=201)
def create_user(
    data: CreateUserSchema,
    controller: CreateUserController = Depends(get_create_user_controller)
) -> UserResponseSchema:
    return controller.handle(data)

@router.get("/users", response_model=list[UserResponseSchema])
def get_all_users(
    controller: GetAllUsersController = Depends(get_get_all_users_controller)
) -> list[UserResponseSchema]:
    return controller.handle()

@router.get('/health', response_model=dict)
def health() -> dict:
    return {'status': 'ok', 'uptime': 'running'}

