from typing import Optional
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
    subjects: list[str]
    availabilities: list[AddAvailability]
    user_id: str
    notes: Optional[str] = None

class SetAvailability(BaseModel):
    updates: list[AvailabilityEntity]
    deletions: list[AvailabilityEntity]

class SetAvailabilityResponse(BaseModel):
    availabilities: list[AvailabilityResponseSchema]
    notes: Optional[str] = None
    subjects: list[str]

class UpdateAvailabilityRequest(BaseModel):
    user_id: str
    subject_code: Optional[str] = None
    availabilities: list[AddAvailability]
    notes: Optional[str] = None
    

class UpdateAvailabilityResponse(BaseModel):
    message: str