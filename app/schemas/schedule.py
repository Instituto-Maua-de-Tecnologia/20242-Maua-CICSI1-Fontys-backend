from pydantic import BaseModel
from sqlalchemy import DateTime

from app.enums.days_of_week_enum import DayOfWeek


class ScheduleBase(BaseModel):
    schedule_id: str
    course_id: str
    user_id: str
    slot_id: int
    subject_code: str
    number_semester: int
    created_at: DateTime