from app.domain.entities.availability_entity import AvailabilityEntity
from sqlalchemy.orm import Session
from app.repositories.availability_repository import AvailabilityRepository


class AvailabilityService:
    def __init__(self, db: Session):
        self.repository = AvailabilityRepository(db)

    def update_availabilities(self, availabilities: list[AvailabilityEntity], notes: str, subject_code: list[str], user_id: str):
        try:
            self.availability_repository.update_availabilities(availabilities, notes, subject_code, user_id)
            return {"message": "Availabilities updated successfully"}
        except Exception as e:
            raise ValueError(f"Error updating availabilities: {str(e)}")
