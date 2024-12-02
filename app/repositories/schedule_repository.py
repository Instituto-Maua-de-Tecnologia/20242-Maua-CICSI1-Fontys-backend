from sqlalchemy import text
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
    
    def create_schedule(self, schedule: ScheduleEntity) -> ScheduleEntity:
        # Criação do cronograma no banco de dados
        db_schedule = Schedule(
            course_id=schedule.course_id,
            user_id=schedule.user_id,
            slot_id=schedule.slot_id,
            subject_code=schedule.subject_code,
            semester_number=schedule.semester_number,
            created_at=schedule.created_at 
        )
        
        try:
            # Adiciona o cronograma ao banco de dados
            self.db.add(db_schedule)
            self.db.commit()
            self.db.refresh(db_schedule)
                    
        except Exception as e:
            # Se ocorrer algum erro, faz rollback da transação
            self.db.rollback()
            raise RuntimeError("Error creating schedule.") from e
        
        # Retorna o cronograma criado e seu tipo associado
        return ScheduleEntity(
            course_id=db_schedule.course_id,
            user_id=db_schedule.user_id,
            slot_id=db_schedule.slot_id,
            subject_code=db_schedule.subject_code,
            semester_number=db_schedule.semester_number,
            created_at=db_schedule.created_at
        )
    def generate_schedule(self):
        try:
            query = text("""
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
