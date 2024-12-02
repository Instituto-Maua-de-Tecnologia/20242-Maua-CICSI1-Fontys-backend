from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.controllers.schedule_controller.create_schedule_IA_controller import CreateScheduleIAController
from app.controllers.schedule_controller.create_schedule_controller import CreateScheduleController
from app.controllers.schedule_controller.generate_schedule_controller import GenerateScheduleController
from app.core.database import get_db
from app.schemas.schedule import GenerateScheduleSchema, ScheduleResponseSchema
from app.services.schedule_services.create_schedule_IA_service import CreateScheduleIAService
from app.services.schedule_services.create_schedule_service import CreateScheduleService
from app.services.schedule_services.generate_schedule_service import GenerateScheduleService


router = APIRouter()

def get_create_schedule_IA_controller(db: Session = Depends(get_db)) -> CreateScheduleIAController:
    service = CreateScheduleIAService(db)
    return CreateScheduleIAController(service)

def get_create_schedule_controller(db: Session = Depends(get_db)) -> CreateScheduleController:
    service = CreateScheduleService(db)
    return CreateScheduleController(service)

def get_generate_schedule_controller(db: Session = Depends(get_db)) -> GenerateScheduleController:
    service = GenerateScheduleService(db)
    return GenerateScheduleController(service)


@router.post("/schedule_IA", response_model=ScheduleResponseSchema ,status_code=201)
def create_schedule_IA(
    data: ScheduleResponseSchema,
    controller: CreateScheduleIAController = Depends(get_create_schedule_IA_controller)
) -> ScheduleResponseSchema:
    return controller.handle(data)

@router.post("/schedule", response_model=ScheduleResponseSchema ,status_code=201)
def create_schedule(
    data: ScheduleResponseSchema,
    controller: CreateScheduleController = Depends(get_create_schedule_controller)
) -> ScheduleResponseSchema:
    return controller.handle(data)

@router.get("/schedule", response_model=list[GenerateScheduleSchema] ,status_code=200)
def generate_schedule(
    controller: GenerateScheduleController = Depends(get_generate_schedule_controller)
) -> list[GenerateScheduleSchema]:
    return controller.handle()