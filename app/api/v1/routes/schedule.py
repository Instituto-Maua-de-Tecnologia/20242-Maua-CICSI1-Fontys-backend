from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.controllers.schedule_controller.create_schedule_IA_controller import CreateScheduleIAController
from app.controllers.schedule_controller.get_schedule_by_id_controller import GetScheduleByIdController
from app.controllers.schedule_controller.publish_schedule_controller import PublishScheduleController
from app.controllers.schedule_controller.generate_schedule_controller import GenerateScheduleController
from app.core.database import get_db
from app.schemas.schedule import GenerateScheduleSchema, GetScheduleSchema, ScheduleEntitySchemaRequest, ScheduleResponseSchema
from app.services.schedule_services.create_schedule_IA_service import CreateScheduleIAService
from app.services.schedule_services.get_schedule_by_id import GetScheduleByIdService
from app.services.schedule_services.publish_schedule_service import PublishScheduleService
from app.services.schedule_services.generate_schedule_service import GenerateScheduleService


router = APIRouter()

def get_create_schedule_IA_controller(db: Session = Depends(get_db)) -> CreateScheduleIAController:
    service = CreateScheduleIAService(db)
    return CreateScheduleIAController(service)

def get_generate_schedule_controller(db: Session = Depends(get_db)) -> GenerateScheduleController:
    service = GenerateScheduleService(db)
    return GenerateScheduleController(service)

def get_publish_schedule_controller(db: Session = Depends(get_db)) -> PublishScheduleController:
    service = PublishScheduleService(db)
    return PublishScheduleController(service)

def get_schedule_by_id_controller(db: Session = Depends(get_db)) -> GetScheduleByIdController:
    service = GetScheduleByIdService(session=db)
    return GetScheduleByIdController(service)


@router.post("/schedule_IA", response_model=ScheduleResponseSchema ,status_code=201)
def create_schedule_IA(
    data: ScheduleResponseSchema,
    controller: CreateScheduleIAController = Depends(get_create_schedule_IA_controller)
) -> ScheduleResponseSchema:
    return controller.handle(data)

@router.get("/schedule", response_model=list[GenerateScheduleSchema] ,status_code=200)
def generate_schedule(
    semester_number: int,
    controller: GenerateScheduleController = Depends(get_generate_schedule_controller)
) -> list[GenerateScheduleSchema]:
    return controller.handle(semester_number=semester_number)

@router.post("/schedule", response_model=ScheduleResponseSchema ,status_code=201)
def publish_schedule(
    schedules: list[ScheduleEntitySchemaRequest], 
    controller: PublishScheduleController = Depends(get_publish_schedule_controller)
    ) -> dict:
    return controller.handle(schedules)

@router.get('/schedule/by-id', response_model=GetScheduleSchema, status_code=200)
def get_schedule_by_id(
    schedule_id: str,
    controller: GetScheduleByIdController = Depends(get_schedule_by_id_controller)
) -> dict:
    return controller.handle(schedule_id)