from typing import Optional
from pydantic import BaseModel

from app.domain.entities.slot_entity import SlotEntity
from app.domain.entities.user_entity import UserEntity
from app.enums.availability_values_enum import AvailabilityValuesEnum
from app.models import Availability


class AvailabilityEntity(BaseModel):
    availability_id: Optional[str] = None
    user: UserEntity
    slot: SlotEntity
    value: AvailabilityValuesEnum

    def to_orm(self) -> Availability:
        return Availability(
            availability_id=self.availability_id or None,
            slot_id=self.slot.slot_id,
            user_id=self.user.user_id,
            availability_value=self.value
        )
