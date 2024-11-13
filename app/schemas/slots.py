

from pydantic import BaseModel
from sqlalchemy import Time

from app.enum.days_of_week import DayOfWeek


class Slot(BaseModel):
    slot_id: str
    day_of_week: DayOfWeek
    time: Time
    