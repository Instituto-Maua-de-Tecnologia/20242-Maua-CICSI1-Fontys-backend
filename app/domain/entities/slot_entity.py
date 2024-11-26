from typing import Optional
from sqlalchemy import Time
from pydantic import BaseModel

from app.enums.days_of_week import DayOfWeek


class SlotEntity(BaseModel):
    slot_id: Optional[int] = True
    day_of_week: DayOfWeek
    time: Time
