from sqlalchemy.orm import Session
from app.repositories.schedule_repository import ScheduleRepository
from app.domain.entities.schedule_entity import ScheduleEntity

class UploadScheduleService:
    def __init__(self, db: Session):
        self.repository = ScheduleRepository(db)

    def execute(self, schedule_data: ScheduleEntity):
        return self.repository.upload_schedule(schedule_data)