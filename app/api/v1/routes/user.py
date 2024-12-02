from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from app.controllers.user_controller.get_all_professors_controller import GetAllProfessorsController
from app.controllers.user_controller.upload_excel_controller import UploadExcelController
from app.core.database import get_db
from app.schemas.user import CreateUserSchema, GetAllProfessorsResponseSchema, UserResponseSchema

from app.services.user_services.upload_excel_service import ReadExcelService
from app.services.user_services.create_user_service import CreateUserService
from app.controllers.user_controller.create_user_controller import CreateUserController
from app.services.user_services.get_all_professors_service import GetAllProfessorsService

router = APIRouter()

# Dependency to get CreateUserController
def get_create_user_controller(db: Session = Depends(get_db)) -> CreateUserController:
    service = CreateUserService(db)
    return CreateUserController(service)

# Dependency to get GetAllProfessorsController
def get_all_professors_controller(db: Session = Depends(get_db)) -> GetAllProfessorsController:
    service = GetAllProfessorsService(db)
    return GetAllProfessorsController(service)

# Dependency to get UploadExcelController
def get_upload_excel_controller() -> UploadExcelController:
    service = ReadExcelService()
    return UploadExcelController(service)

# Route to create a new user
@router.post("/users/create-user", response_model=UserResponseSchema, status_code=201)
def create_user(
    data: CreateUserSchema,
    controller: CreateUserController = Depends(get_create_user_controller)
) -> UserResponseSchema:
    return controller.handle(data)

# Route to get all professors
@router.get("/users", response_model=list[GetAllProfessorsResponseSchema], status_code=200)
def get_all_professors(
    controller: GetAllProfessorsController = Depends(get_all_professors_controller)
) -> list[GetAllProfessorsResponseSchema]:
    return controller.handle()

# Health check route

@router.get('/health', response_model=dict) 
def health() -> dict:
    return {'status': 'ok', 'uptime': 'running'}

# Route to upload Excel file
@router.post("/upload_excel/")
async def upload_excel(
    file: UploadFile = File(...),
    controller: UploadExcelController = Depends(get_upload_excel_controller)
):
    return await controller.handle(file)
