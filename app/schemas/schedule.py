from pydantic import BaseModel

from app.enum.days_of_week import DayOfWeek


class Schedule(BaseModel):
    schedule_id: str
    professor_id: str
    day_of_week: DayOfWeek
    start_time: str