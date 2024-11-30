from typing import Optional
from pydantic import BaseModel

from app.domain.entities.slot_entity import SlotEntity
from app.domain.entities.user_entity import UserEntity
from app.enums.availability_values_enum import AvailabilityValuesEnum

class AvailabilityEntity(BaseModel):
    availability_id: Optional[str] = None
    user: UserEntity
    slot: SlotEntity
    value: AvailabilityValuesEnum
