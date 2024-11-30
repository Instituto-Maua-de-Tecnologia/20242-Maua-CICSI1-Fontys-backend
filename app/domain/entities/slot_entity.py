from typing import Optional

from pydantic import BaseModel

from app.enums.days_of_week_enum import DayOfWeekEnum
from app.enums.time_slot_enum import TimeSlotEnum


class SlotEntity(BaseModel):
    slot_id: Optional[int] = None
    day_of_week: Optional[DayOfWeekEnum] = None
    time: Optional[TimeSlotEnum] = None
