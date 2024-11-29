from typing import Optional
from app.domain.entities.schedule_entity import ScheduleEntity
from app.services.schedule_services.get_schedule_by_id_service import GetScheduleByIdService

class UploadScheduleController:

    def __init__(self, service: GetScheduleByIdService):
        self.service = service

    def handle(self, schedule_entity: ScheduleEntity) -> Optional[str]:
        response = self.service.execute(
            ScheduleEntity
        )

        return response