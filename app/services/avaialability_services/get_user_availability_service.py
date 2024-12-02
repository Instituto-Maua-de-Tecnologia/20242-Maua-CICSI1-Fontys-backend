from app.domain.entities.availability_entity import AvailabilityEntity
from app.repositories.availability_repository import AvailabilityRepository
from sqlalchemy.orm.session import Session

from app.repositories.slot_repository import SlotRepository
from app.repositories.user_repository import UserRepository

class GetUserAvailabilityService:
 def __init__(self, db: Session) -> None:
        self.availability_repository = AvailabilityRepository(db)
        
def get_user_availability(self, user_id: str) -> list[AvailabilityEntity]:
    return self.availability_repository.get_availability_by_user_id(user_id)