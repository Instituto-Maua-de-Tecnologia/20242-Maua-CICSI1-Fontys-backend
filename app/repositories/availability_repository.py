from sqlalchemy.orm import Session
from app.models.availabilities import Availability

class AvailabilityRepository:
    def set_availability(self, availabilities: list[Availability], user_id: str, db: Session) -> list[Availability]:
        db.query(Availability).filter_by(user_id=user_id).delete()

        new_availabilities = []
        for a in availabilities:
            new_availability = Availability(
                user_id=user_id,
                slot_id=a.slot_id,
                availability_value=a.availability_value,
            )
            db.add(new_availability)
            new_availabilities.append(new_availability)

        db.commit()

        return new_availabilities

    def get_availability_by_user_id(self, user_id: int, db: Session) -> list[Availability]:
        return db.query(Availability).filter_by(user_id=user_id).all()
