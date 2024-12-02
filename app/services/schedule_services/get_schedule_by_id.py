
from sqlalchemy.orm import Session

from app.repositories.schedule_repository import ScheduleRepository


class GetScheduleByIdService:
    def __init__(self, session: Session):
        self.repo = ScheduleRepository(db=session)

    def execute(self, schedule_id: str):
        if not schedule_id:
            raise ValueError('Missing schedule id for getting it.')
        
        schedule = self.repo.get_schedule_by_id(schedule_id)

        if not schedule:
            raise ValueError('Something went wrong on getting schedule by id')

        return schedule

        
    

