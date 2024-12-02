from sqlalchemy.orm import Session

from app.repositories.schedule_repository import ScheduleRepository


class GenerateScheduleService:
    def __init__ (self, db: Session):
        self.schedule_repository = ScheduleRepository(db)

    def execute(self):
        response = self.schedule_repository.generate_schedule()
        return response