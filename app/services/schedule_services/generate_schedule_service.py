from sqlalchemy.orm import Session

from app.repositories.schedule_repository import ScheduleRepository


class GenerateScheduleService:
    def _init (self, db: Session):
        self.schedule_repository = ScheduleRepository(db)

    def execute(self, semester_number: int):
        response = self.schedule_repository.generate_schedule(semester_number=semester_number)
        return response