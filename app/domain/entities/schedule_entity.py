from typing import Optional
import uuid
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy import DateTime

from app.models.schedules import Schedule

class ScheduleEntity(BaseModel):
    course_id: str                              # ID do curso relacionado
    user_id: str                                # ID do professor/usuário
    slot_id: int                                # ID do slot
    subject_code: str                           # Código da matéria
    number_semester: Optional[int] = None       # Número do semestre
    created_at: Optional[datetime] = None       # Data de criação do cronograma             
        
    def to_orm(self) -> Schedule:
        return Schedule(
            schedule_id=self.get("schedule_id", str(uuid.uuid4())),
            course_id=self.course_id,
            user_id=self.user_id,
            slot_id=self.slot_id,
            subject_code=self.subject_code,
            number_semester=self.number_semester,
            created_at=self.get("created_at", datetime.utcnow()),
        )    

    
    @classmethod
    def from_dict(cls, data: Schedule) -> "ScheduleEntity":
        """Cria uma instância da entidade a partir de um dicionário"""
        return cls(
            course_id=data.course_id,
            user_id=data.user_id,
            slot_id=data.slot_id,
            subject_code=data.subject_code,
            number_semester=data.number_semester,
            created_at=data.created_at
        )

    def to_dict(self) -> dict:
        """Converte a entidade em um dicionário, que pode ser usado em APIs ou banco de dados"""
        return {
            "course_id": self.course_id,
            "user_id": self.user_id,
            "slot_id": self.slot_id,
            "subject_code": self.subject_code,
            "number_semester": self.number_semester,
            "created_at": self.created_at
        }
    
