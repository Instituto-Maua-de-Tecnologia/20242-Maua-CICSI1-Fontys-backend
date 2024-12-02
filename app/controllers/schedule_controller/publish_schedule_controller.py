from fastapi import HTTPException
from app.domain.entities.schedule_entity import ScheduleEntity
from app.services.schedule_services.publish_schedule_service import PublishScheduleService

class PublishScheduleController:
    def __init__(self, schedule_service: PublishScheduleService):
        self.schedule_service = schedule_service

    def publish_schedule(self, schedules: list[ScheduleEntity]) -> dict:
        try:
            message = self.publish_schedule_service.execute(schedules)
            return {"message": message}
        except RuntimeError as e:
            raise HTTPException(status_code=500, detail=str(e))
