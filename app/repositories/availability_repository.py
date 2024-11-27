from sqlalchemy.orm import Session

from app.domain.entities.availability_entity import AvailabilityEntity
from app.models.availabilities import Availability
from app.repositories.slot_repository import SlotRepository
from app.repositories.user_repository import UserRepository


class AvailabilityRepository:
    def __init__(self, db: Session, user_repo: UserRepository, slot_repo: SlotRepository):
        self.db = db
        self.user_repo = user_repo
        self.slot_repo = slot_repo

    def set_availability(self, availabilities: list[AvailabilityEntity], user_id: str) -> list[AvailabilityEntity]:
        self.db.query(Availability).filter_by(user_id=user_id).delete()

        new_availabilities = []
        for a in availabilities:
            new_availability = Availability(
                user_id=user_id,
                slot_id=a.slot.slot_id,
                availability_value=a.value,
            )
            self.db.add(new_availability)
            new_availabilities.append(new_availability)

        self.db.commit()

        return availabilities

    def get_availability_by_user_id(self, user_id: str) -> list[AvailabilityEntity]:
        availability =  self.db.query(Availability).filter_by(user_id=user_id).all()
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
