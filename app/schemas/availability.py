from pydantic import BaseModel

from app.enums.availability_values import AvailabilityValues

class AvailabilityBase(BaseModel):
    availability_id: str
    user_id: str
    slot_id: int
    value: AvailabilityValues

class GetUserAvailabilityRequest(BaseModel):
    user_id: str