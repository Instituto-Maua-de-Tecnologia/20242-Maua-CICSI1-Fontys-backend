from pydantic import BaseModel

from app.enums.time_slot import TimeSlot
from app.enums.availability_values import Values


class AvailabilityBase(BaseModel):
    availability_id: str
    user_id: str
    slot_id: int
    value: Values