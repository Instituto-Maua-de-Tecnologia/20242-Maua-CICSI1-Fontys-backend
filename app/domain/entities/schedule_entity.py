from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy import DateTime

from app.models.schedules import Schedule

class ScheduleEntity(BaseModel):
    schedule_id: Optional[str] = None           # Identificador único do cronograma
    course_id: Optional[str] = None             # ID do curso relacionado
    user_id: Optional[str] = None               # ID do professor/usuário
    slot_id: Optional[int] = None               # ID do slot
    subject_code: Optional[str] = None          # Código da matéria
    number_semester: Optional[int] = None       # Número do semestre
    created_at: Optional[datetime] = None       # Data de criação do cronograma
    day_of_week: Optional[str] = None           # Dia da semana (ex: "Segunda-feira")
    time: Optional[str] = None                  # Hora de início do slot (formato 'HH:MM')             
        
    def to_orm(self) -> Schedule:
        """Converte a entidade em um objeto ORM"""
        return Schedule(
            schedule_id=self.schedule_id,
            course_id=self.course_id,
            user_id=self.user_id,
            slot_id=self.slot_id,
            subject_code=self.subject_code,
            number_semester=self.number_semester,
            created_at=self.created_at,
            day_of_week=self.day_of_week,
            time=self.time
        )    

    
    @classmethod
    def from_dict(cls, data: Schedule) -> "ScheduleEntity":
        """Cria uma instância da entidade a partir de um dicionário"""
        return cls(**data)

    def to_dict(self) -> dict:
        """Converte a entidade em um dicionário, que pode ser usado em APIs ou banco de dados"""
        return {
            "schedule_id": self.schedule_id,
            "course_id": self.course_id,
            "user_id": self.user_id,
            "slot_id": self.slot_id,
            "subject_code": self.subject_code,
            "number_semester": self.number_semester,
            "created_at": self.created_at,
            "day_of_week": self.day_of_week,
            "time": self.time
        }
    
