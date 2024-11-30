from pydantic import BaseModel

from app.enums.days_of_week_enum import DayOfWeekEnum
from app.enums.time_slot_enum import TimeSlotEnum


class SlotBase(BaseModel):
    slot_id: int
    day_of_week: DayOfWeekEnum
    time: TimeSlotEnum
    