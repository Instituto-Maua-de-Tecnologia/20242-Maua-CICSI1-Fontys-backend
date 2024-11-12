from pydantic import BaseModel

from app.enum.days_of_week import DayOfWeek


class Schedule(BaseModel):
    schedule_id: str
    course_id: str
    user_id: str
    slot_id: str
    subject_code: str
    number_semester: int