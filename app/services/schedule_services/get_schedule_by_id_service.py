from sqlalchemy.orm import Session
from app.repositories.schedule_repository import ScheduleRepository
from app.domain.entities.schedule_entity import ScheduleEntity

class GetScheduleByIdService:
    def __init__(self, db: Session):
        self.repository = ScheduleRepository(db)

    def execute(self, schedule_id):
        return self.repository.get_schedule_by_id(schedule_id)