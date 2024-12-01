from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.controllers.slot_controller.get_slots_controller import GetSlotsController
from app.core.database import SessionLocal
from app.schemas.slots import SlotBase
from app.services.slot_service import SlotService

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_slots_controller(db: Session = Depends(get_db)) -> GetSlotsController:
    service = SlotService(db)
    return GetSlotsController(service)

@router.get("/slots/", response_model=List[SlotBase])
def get_slots(
        controller: GetSlotsController = Depends(get_slots_controller)
) -> List[SlotBase]:
    return controller.handle()