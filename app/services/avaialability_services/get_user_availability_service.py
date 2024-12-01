from app.domain.entities.availability_entity import AvailabilityEntity
from app.repositories.availability_repository import AvailabilityRepository
from sqlalchemy.orm.session import Session

class GetUserAvailabilityService:
 def __init__(self, db: Session) -> None:
        self.availability_repository = AvailabilityRepository(db, self.user_repository, self.slot_repository)
        
def get_user_availability(self, user_id: str) -> list[AvailabilityEntity]:
    return self.availability_repository.get_availability_by_user_id(user_id)