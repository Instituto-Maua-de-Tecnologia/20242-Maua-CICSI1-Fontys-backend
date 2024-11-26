from typing import Optional
from xmlrpc.client import DateTime

from pydantic import BaseModel

from app.enums.days_of_week import DayOfWeek


class SlotEntity(BaseModel):
    slot_id: Optional[int] = True
    day_of_week: DayOfWeek
    time: DateTime

    class Config:
        arbitrary_types_allowed = True
