import json

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.controllers.schedule_controller.create_schedule_IA_controller import CreateScheduleIAController
from app.controllers.schedule_controller.upload_schedule_controller import UploadScheduleController
from app.controllers.schedule_controller.get_schedule_by_id_controller import GetScheduleByIdController
from app.core.database import get_db
from app.schemas.schedule import ScheduleResponseSchema
from app.services.schedule_services.create_schedule_IA_service import CreateScheduleIAService
from app.services.schedule_services.upload_schedule_service import UploadScheduleService
from app.services.schedule_services.get_schedule_by_id_service import GetScheduleByIdService
from app.services.schedule_generator import ScheduleGenerator


router = APIRouter()

def get_create_schedule_IA_controller(db: Session = Depends(get_db)) -> CreateScheduleIAController:
    service = CreateScheduleIAService(db)
    return CreateScheduleIAController(service)

def get_get_schedule_by_id_controller(db: Session = Depends(get_db)) -> GetScheduleByIdController:
    service = GetScheduleByIdService(db)
    return GetScheduleByIdController(service)

def get_upload_schedule_controller(db: Session = Depends(get_db)) -> UploadScheduleController:
    service = UploadScheduleService(db)
    return UploadScheduleController(service)

@router.post("/schedule_IA", response_model=ScheduleResponseSchema ,status_code=201)
def create_schedule_IA(
    data: ScheduleResponseSchema,
    controller: CreateScheduleIAController = Depends(get_create_schedule_IA_controller)
) -> ScheduleResponseSchema:
    return controller.handle(data)

@router.get("/scheduleById", response_model=ScheduleResponseSchema ,status_code=201)
def get_schedule_by_id(
    data: str,
    controller: GetScheduleByIdController = Depends(get_get_schedule_by_id_controller)
) -> ScheduleResponseSchema:
    return controller.handle(data)

@router.get("/schedule", response_model=ScheduleResponseSchema ,status_code=201)
def generate_schedule(available_teacher_times, subjects, semester):
    return [
        json.dumps(ScheduleGenerator.order_schedule(available_teacher_times, subjects, semester))
    ]

@router.post("/uploadSchedule", response_model=ScheduleResponseSchema ,status_code=201)
def upload_schedule(
    data: ScheduleResponseSchema,
    controller: UploadScheduleController = Depends(get_upload_schedule_controller)
) -> ScheduleResponseSchema:
    return controller.handle(data)