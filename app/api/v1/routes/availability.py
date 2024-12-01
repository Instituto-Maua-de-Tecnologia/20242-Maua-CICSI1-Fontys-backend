from typing import List

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.controllers.availability_controller.get_availability_controller import GetAvailabilityController
from app.controllers.availability_controller.set_availability_controller import SetAvailabilityController
from app.core.database import SessionLocal
from app.schemas.availability import  SetAvailabilityRequest, AvailabilityResponseSchema
from app.services.avaialability_services.set_availability_service import SetAvailabilityService
from app.services.avaialability_services.get_user_availability_service import GetUserAvailabilityService

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_availability_controller(db: Session = Depends(get_db)) -> GetAvailabilityController:
    service = GetUserAvailabilityService(db)
    return GetAvailabilityController(service)

def set_availability_controller(db: Session = Depends(get_db)) -> SetAvailabilityController:
    service = SetAvailabilityService(db)
    return SetAvailabilityController(service)

@router.get("/availability/", response_model=List[AvailabilityResponseSchema])
def get_availability(
        user_id: str = Query(...),
        controller: GetAvailabilityController = Depends(get_availability_controller)
) -> List[AvailabilityResponseSchema]:
    return controller.handle(user_id)

@router.post("/availability/", response_model=List[AvailabilityResponseSchema])
def set_availability(
        data: SetAvailabilityRequest,
        controller: SetAvailabilityController = Depends(set_availability_controller)
) -> List[AvailabilityResponseSchema]:
    return controller.handle(data)

