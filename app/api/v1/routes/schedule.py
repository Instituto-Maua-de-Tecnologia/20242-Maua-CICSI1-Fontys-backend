from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.services.schedule_generator import ScheduleGenerator
from app.core.database import get_db
from app.domain.entities.schedule_entity import ScheduleEntity
from app.services.schedule_services.get_schedule_by_id_service import GetScheduleByIdService
from app.services.schedule_services.upload_schedule_service import UploadScheduleService
from app.controllers.schedule_controller.get_schedule_by_id_controller import GetScheduleByIdController
from app.controllers.schedule_controller.upload_schedule_controller import UploadScheduleController
import json

ScheduleRouter = APIRouter(prefix="/schedule")

def get_get_schedule_by_id_controller(db: Session = Depends(get_db)) -> GetScheduleByIdController:
    service = GetScheduleByIdService(db)
    return GetScheduleByIdController(service)

def get_upload_schedule_controller(db: Session = Depends(get_db)) -> UploadScheduleController:
    service = UploadScheduleService(db)
    return UploadScheduleController(service)

@ScheduleRouter.post("/", )
def generate_schedule(available_teacher_times, subjects, semester):
    return [
        json.dumps(ScheduleGenerator.order_schedule(available_teacher_times, subjects, semester))
    ]

@ScheduleRouter.get("/getSchedule", )
def get_schedule_by_id(
        data: str,
        controller: GetScheduleByIdController = Depends(get_get_schedule_by_id_controller)
)-> ScheduleEntity :
    return controller.handle(data)



@ScheduleRouter.post("/uploadSchedule", )
def upload_schedule(
        data: ScheduleEntity,
        controller: UploadScheduleController = Depends(get_upload_schedule_controller)
)-> str :
    return controller.handle(data)

