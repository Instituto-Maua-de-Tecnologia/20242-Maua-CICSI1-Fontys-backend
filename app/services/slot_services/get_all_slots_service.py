from sqlalchemy.orm.session import Session

from app.domain.entities.slot_entity import SlotEntity
from app.repositories.slot_repository import SlotRepository

class GetAllSlotsService:
    def __init__(self, db: Session) -> None:
        self.repository = SlotRepository(db)

    def get_all(self) -> list[SlotEntity]:
        return self.repository.get_all()
