from datetime import datetime
from sqlalchemy import text
from sqlalchemy.orm import Session
from typing import Optional
from app.models.schedules import Schedule
from app.domain.entities.schedule_entity import ScheduleEntity

class ScheduleRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_schedule_by_id(self, schedule_id: str) -> Optional[ScheduleEntity]:
        db_schedule = self.db.query(Schedule).filter(Schedule.schedule_id == schedule_id).first()
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
    
    def publish_schedule(self, schedules: list[ScheduleEntity]) -> ScheduleEntity:
        """
        Salva uma lista de cronogramas gerados no banco de dados.
        """
        try:
            print('entrou no metodo publish schedule')
            print('lista de entidades schedule: ', schedules)
            for schedule in schedules:
                db_schedule = Schedule(
                    user_id=schedule["user_id"],
                    slot_id=schedule["slot_id"],
                    subject_code=schedule["subject_code"],
                    semester_number=schedule["number_semester"],
                    course_id=schedule["course_id"],
                    created_at=datetime.now()
                )

                print('db schedule to be added, ', db_schedule)
                self.db.add(db_schedule)

            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            raise RuntimeError("Error publishing schedules.") from e

        
    def generate_schedule(self, semester_number: int) -> list[dict]:
            try:
                query = text(f"""
                WITH RandomAvailabilitys AS (
                    SELECT 
                        u.user_id,
                        u.name,
                        us.subject_code,
                        s.slot_id,
                        s.day_of_week,
                        s.time,
                        a.availability_value,
                        su.subject_name,
                        se.course_id,
                        se.semester_number,
                        ROW_NUMBER() OVER (PARTITION BY s.day_of_week, s.time ORDER BY RANDOM()) AS rn
                    FROM availabilitys a
                    LEFT JOIN users u ON a.user_id = u.user_id
                    LEFT JOIN user_subjects us ON u.user_id = us.user_id
                    LEFT JOIN slots s ON a.slot_id = s.slot_id
                    LEFT JOIN subjects su ON su.subject_code = us.subject_code
                    LEFT JOIN semesters se ON se.subject_code = su.subject_code
                    WHERE a.availability_value = 'POSSIBLE'
                    AND se.semester_number = {semester_number}
                )
                SELECT 
                    user_id,
                    name, 
                    subject_code, 
                    slot_id,
                    day_of_week, 
                    time,
                    availability_value,
                    subject_name,
                    course_id,
                    semester_number
                FROM RandomAvailabilitys
                WHERE rn = 1;
                """)

                result = self.db.execute(query)
                schedule = [row._asdict() for row in result]
                return schedule
            except Exception as e:
                return str(e)
