from typing import Optional
from app.models.schedules import Schedule
from app.domain.entities.schedule_entity import ScheduleEntity
from app.services.schedule_services.get_schedule_by_id_service import GetScheduleByIdService

class GetScheduleByIdController:

    def __init__(self, service: GetScheduleByIdService):
        self.service = service

    def handle(self, id: str) -> Optional[ScheduleEntity]:
        response = self.service.execute(id)
        return response