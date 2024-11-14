

from pydantic import BaseModel
from sqlalchemy import Time

from app.enums.days_of_week import DayOfWeek


class SlotBase(BaseModel):
    slot_id: int
    day_of_week: DayOfWeek
    time: Time
    