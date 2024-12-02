from sqlalchemy.orm import Session
from app.domain.entities.schedule_entity import ScheduleEntity
from app.repositories.schedule_repository import ScheduleRepository

class CreateScheduleService:
    def __init__(self, db: Session):
        self.schedule_repository = ScheduleRepository(db)

    def execute(self, 
                      course_id: str, 
                      user_id: str, 
                      slot_id: str, 
                      subject_code: str, 
                      semester_number: int, 
                      created_at: str
                ) -> ScheduleEntity:
        
        schedule = ScheduleEntity(
            course_id=course_id,
            user_id=user_id,
            slot_id=slot_id,
            subject_code=subject_code,
            semester_number=semester_number,
            created_at=created_at
        )

        return self.schedule_repository.create_schedule(schedule)