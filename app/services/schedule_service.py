from sqlalchemy.orm import Session
from app.repositories.schedule_repository import ScheduleRepository
from app.domain.entities.schedule_entity import ScheduleEntity

class ScheduleService:
    def __init__(self, db: Session):
        self.repository = ScheduleRepository(db)

    def upload_schedule(self, schedule_data: ScheduleEntity):
        return self.repository.upload_schedule(schedule_data)

    def get_schedule_by_id(self, schedule_id):
        return self.repository.get_schedule_by_id(schedule_id)