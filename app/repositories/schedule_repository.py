from sqlalchemy.orm import Session
from typing import Optional
from app.models.schedules import Schedule
from app.domain.interfaces.repositories.schedule_repository_interface import IScheduleRepository
from app.domain.entities.schedule_entity import ScheduleEntity

class ScheduleRepository(IScheduleRepository):
    def __init__(self, db: Session):
        self.db = db

    def upload_schedule(self, schedule_entity: ScheduleEntity) -> Optional[str]:
        db_schedule = Schedule(
            schedule_id=schedule_entity.schedule_id,
            course_id=schedule_entity.course_id,
            user_id=schedule_entity.user_id,
            slot_id=schedule_entity.slot_id,
            subject_code=schedule_entity.subject_code,
            semester_number=schedule_entity.semester_number,
            created_at=schedule_entity.created_at
        )

        try:
            self.db.add(db_schedule)
            self.db.commit()
            self.db.refresh(db_schedule)
            return None
        except:
            return "something went wrong when uploading the schedule"


    def get_schedule_by_id(self, id: str) -> Optional[ScheduleEntity]:
        db_schedule = self.db.query(Schedule).filter(Schedule.schedule_id == id).first()
        if db_schedule:
            return ScheduleEntity(
                schedule_id=db_schedule.schedule_id,
                course_id=db_schedule.course_id,
                user_id=db_schedule.user_id,
                slot_id=db_schedule.slot_id,
                subject_code=db_schedule.subject_code,
                number_semester=db_schedule.semester_number,
                created_at=db_schedule.created_at
            )
        return None