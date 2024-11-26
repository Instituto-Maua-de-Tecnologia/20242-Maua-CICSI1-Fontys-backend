from sqlalchemy.orm.session import Session

from app.domain.entities.availability_entity import AvailabilityEntity
from app.models.availabilities import Availability
from app.repositories.availability_repository import AvailabilityRepository

class AvailabilityService:
    def __init__(self, availability_repository: AvailabilityRepository, db: Session) -> None:
        self.availability_repository = availability_repository
        self.db = db

    def set_availability(self, availabilities: list[AvailabilityEntity], user_id: str) -> list[AvailabilityEntity]:
        return self.availability_repository.set_availability(availabilities, user_id)

    def get_user_availability(self, user_id: str) -> list[AvailabilityEntity]:
        return self.availability_repository.get_availability_by_user_id(user_id)
