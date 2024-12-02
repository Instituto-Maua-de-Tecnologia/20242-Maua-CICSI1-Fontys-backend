from datetime import datetime

from sqlalchemy.orm import Session

from app.domain.entities.availability_entity import AvailabilityEntity
from app.models.availabilities import Availability
from app.models.users import User
from app.repositories.slot_repository import SlotRepository
from app.repositories.user_repository import UserRepository
from app.schemas.availability import SetAvailability


class AvailabilityRepository:
    def __init__(self, db: Session, user_repo: UserRepository, slot_repo: SlotRepository):
        self.db = db
        self.user_repo = user_repo
        self.slot_repo = slot_repo

    def apply_changes(self, changes: SetAvailability, user_id: str) -> list[AvailabilityEntity]:
        to_delete = []
        for update in changes.updates:
            record = Availability(
                availability_id=update.availability_id or None,
                slot_id=update.slot.slot_id,
                user_id=user_id,
                availability_value=update.value,
                created_at=datetime.now()
            )
            self.db.merge(record)

        for delete in changes.deletions:
            to_delete.append(delete.availability_id)

        if to_delete:
            (self.db.query(Availability)
             .filter(Availability.availability_id.in_(to_delete))
             .delete(synchronize_session=False))

        self.db.commit()

        return changes.updates

    def get_availability_by_user_id(self, user_id: str) -> list[AvailabilityEntity]:
        availability = self.db.query(Availability).filter_by(user_id=user_id).all()
        user = self.user_repo.get_by_id(user_id)

        entities = []
        for a in availability:
            slot = self.slot_repo.get_by_id(a.slot_id)
            a = AvailabilityEntity(
                availability_id = a.availability_id,
                user = user,
                slot = slot,
                value = a.availability_value,
            )
            entities.append(a)
        return entities
