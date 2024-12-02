from sqlalchemy.orm import Session
from app.domain.entities.schedule_entity import ScheduleEntity
from app.repositories.schedule_repository import ScheduleRepository

class PublishScheduleService:
    def __init__(self, db: Session):
        self.schedule_repository = ScheduleRepository(db)
        
    def execute(self, schedules: list[ScheduleEntity]) -> str:

        if not schedules:
            return "No schedules provided in the request body."

        # Publica os cronogramas
        try:
            is_published = self.schedule_repository.publish_schedule(schedules)
            if is_published:
                return "Schedules published successfully."
        except Exception as e:
            raise RuntimeError(f"Failed to publish schedules: {str(e)}")