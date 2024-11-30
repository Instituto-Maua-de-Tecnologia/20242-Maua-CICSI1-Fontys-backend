from typing import Optional
from xmlrpc.client import DateTime

from pydantic import BaseModel

from app.enums.days_of_week_enum import DayOfWeekEnum


class SlotEntity(BaseModel):
    slot_id: Optional[int] = None
    day_of_week: DayOfWeekEnum
    time: DateTime

    class Config:
        arbitrary_types_allowed = True
