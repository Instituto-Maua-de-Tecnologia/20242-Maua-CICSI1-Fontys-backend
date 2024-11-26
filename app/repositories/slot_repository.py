from sqlalchemy.orm import Session
from app.domain.entities.slot_entity import SlotEntity
from app.models.slots import Slot


class SlotRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, slot_id: int) -> SlotEntity:
        slot = self.db.query(Slot).filter_by(slot_id=slot_id).first()
        return SlotEntity(
            slot_id = slot.slot_id,
            day_of_week=slot.day_of_week,
            time=slot.time
        )