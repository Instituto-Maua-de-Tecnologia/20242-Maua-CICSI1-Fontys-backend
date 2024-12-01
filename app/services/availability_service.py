from sqlalchemy.orm.session import Session

from app.domain.entities.availability_entity import AvailabilityEntity
from app.domain.entities.slot_entity import SlotEntity
from app.repositories.availability_repository import AvailabilityRepository
from app.repositories.slot_repository import SlotRepository
from app.repositories.user_repository import UserRepository
from app.schemas.availability import AddAvailability, SetAvailability


class AvailabilityService:
    def __init__(self, db: Session) -> None:
        self.user_repository = UserRepository(db)
        self.slot_repository = SlotRepository(db)
        self.availability_repository = AvailabilityRepository(db, self.user_repository, self.slot_repository)

    def set_availability(self, availabilities: list[AddAvailability], user_id: str) -> list[AvailabilityEntity]:
        user = self.user_repository.get_by_id(user_id)
        current_availabilities = self.availability_repository.get_availability_by_user_id(user_id)

        current_map = {}
        for a in current_availabilities:
            current_map[a.slot.slot_id] = a
        incoming_map = {}
        for a in availabilities:
            incoming_map[a.slot_id] = a

        changes = SetAvailability(
            updates = [],
            deletions =[],
        )

        for a in availabilities:
            if a.slot_id in current_map:
                existing = current_map[a.slot_id]
                existing.value = a.value
                changes.updates.append(existing)
            else:
                slot = SlotEntity(slot_id=a.slot_id)
                changes.updates.append(AvailabilityEntity(user=user, slot=slot, value=a.value))

        for c in current_availabilities:
            if c.slot.slot_id not in incoming_map:
                changes.deletions.append(c)

        return self.availability_repository.apply_changes(changes, user_id)

    def get_user_availability(self, user_id: str) -> list[AvailabilityEntity]:
        return self.availability_repository.get_availability_by_user_id(user_id)
