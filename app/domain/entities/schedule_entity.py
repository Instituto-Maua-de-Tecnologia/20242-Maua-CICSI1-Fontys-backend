from typing import Optional
from pydantic import BaseModel
from sqlalchemy import DateTime

class ScheduleEntity(BaseModel):
    schedule_id: Optional[str] = None
    course_id: Optional[str] = None
    user_id: Optional[str] = None
    slot_id: Optional[int] = None
    subject_code: Optional[str] = None
    number_semester: Optional[int] = None
    created_at: Optional[DateTime] = None