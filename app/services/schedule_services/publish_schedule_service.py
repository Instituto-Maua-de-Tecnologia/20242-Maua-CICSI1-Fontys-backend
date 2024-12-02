from sqlalchemy.orm import Session
from app.domain.entities.schedule_entity import ScheduleEntity
from app.repositories.schedule_repository import ScheduleRepository

class PublishScheduleService:
    def __init__(self, db: Session):
        self.schedule_repository = ScheduleRepository(db)
        
    def execute(self, schedules: list[ScheduleEntity]) -> str:

        if not schedules:
            print('publish service, case if not schedules')
            return "No schedules provided in the request body."

        # Publica os cronogramas
        try:
            print('inside try / except publish service')
            is_published = self.schedule_repository.publish_schedule(schedules)
            print('passou do acesso ao banco no repository')
            if is_published:
                return "Schedules published successfully."
        except Exception as e:
            raise RuntimeError(f"Failed to publish schedules: {str(e)}")