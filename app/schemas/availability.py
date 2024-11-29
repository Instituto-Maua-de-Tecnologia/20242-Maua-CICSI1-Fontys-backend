from pydantic import BaseModel
from app.enums.availability_values_enum import AvailabilityValuesEnum


class AvailabilityBase(BaseModel):
    availability_id: str
    user_id: str
    slot_id: int
    value: AvailabilityValuesEnum