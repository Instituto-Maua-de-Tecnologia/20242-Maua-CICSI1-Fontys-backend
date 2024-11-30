from pydantic import BaseModel

from app.domain.entities.availability_entity import AvailabilityEntity
from app.enums.availability_values_enum import AvailabilityValuesEnum


class AvailabilityBase(BaseModel):
    availability_id: str
    user_id: str
    slot_id: int
    value: AvailabilityValuesEnum

class AvailabilityResponseSchema(BaseModel):
    slot_id: int
    value: AvailabilityValuesEnum

class GetUserAvailabilityRequest(BaseModel):
    user_id: str

class AddAvailability(BaseModel):
    slot_id: int
    value: AvailabilityValuesEnum

class SetAvailabilityRequest(BaseModel):
    availabilities: list[AddAvailability]
    user_id: str

class SetAvailability(BaseModel):
    updates: list[AvailabilityEntity]
    deletions: list[AvailabilityEntity]
