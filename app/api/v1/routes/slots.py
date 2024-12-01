from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.controllers.slot_controller.get_all_slots_controller import GetAllSlotsController
from app.core.database import SessionLocal
from app.schemas.slots import SlotBase
from app.services.slot_services.get_all_slots_service import GetAllSlotsService

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_slots_controller(db: Session = Depends(get_db)) -> GetAllSlotsController:
    service = GetAllSlotsService(db)
    return GetAllSlotsController(service)

@router.get("/slots/", response_model=List[SlotBase])
def get_slots(
        controller: GetAllSlotsController = Depends(get_slots_controller)
) -> List[SlotBase]:
    return controller.handle()