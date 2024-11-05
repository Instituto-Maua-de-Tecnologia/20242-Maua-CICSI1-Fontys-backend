from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.availability import Availability
from app.schemas.user import User

class AvailabilityRepository:
	def create_availability(self, availability: Availability, db: Session) -> Availability:
		new_availability = Availability(
			availability_id="",
			user_id="1", #Temporarily hard coded
			day_of_week=availability.day_of_week,
			time_slot=availability.time_slot,
			status=availability.status
		)
		db.add(new_availability)
		db.commit()
		db.refresh(new_availability)
		return new_availability

	def get_availability_by_user_id(self, user_id: str, db: Session) -> list[Availability]:
		return db.query(Availability).filter_by(user_id=user_id).all()
