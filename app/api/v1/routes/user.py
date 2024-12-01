from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from app.controllers.user_controller.get_all_professors_controller import GetAllProfessorsController
from app.core.database import get_db
from app.schemas.user import CreateUserSchema, GetAllProfessorsResponseSchema, UserResponseSchema
from app.services.user_services.create_user_service import CreateUserService
from app.controllers.user_controller.create_user_controller import CreateUserController
from app.services.user_services.get_all_professors_service import GetAllProfessorsService


router = APIRouter()

def get_create_user_controller(db: Session = Depends(get_db)) -> CreateUserController:
    service = CreateUserService(db)
    return CreateUserController(service)


def get_all_professors_controller(db: Session = Depends(get_db)) -> GetAllProfessorsController:
    service = GetAllProfessorsService(db)
    return GetAllProfessorsController(service)


@router.post("/users", response_model=UserResponseSchema, status_code=201)
def create_user(
    data: CreateUserSchema,
    controller: CreateUserController = Depends(get_create_user_controller)
) -> UserResponseSchema:
    return controller.handle(data)

@router.get("/users", response_model=list[GetAllProfessorsResponseSchema], status_code=200)
def get_all_professors(
    controller: GetAllProfessorsController = Depends(get_all_professors_controller)
) -> list[GetAllProfessorsResponseSchema]:
    return controller.handle()

@router.get('/health', response_model=dict)
def health() -> dict:
    return {'status': 'ok', 'uptime': 'running'}

