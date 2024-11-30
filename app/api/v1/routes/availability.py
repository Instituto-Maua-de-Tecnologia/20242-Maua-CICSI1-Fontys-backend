from typing import List
from warnings import deprecated

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.controllers.availability_controller.get_availability_controller import GetAvailabilityController
from app.controllers.availability_controller.set_availability_controller import SetAvailabilityController
from app.core.database import SessionLocal
from app.schemas.availability import  SetAvailabilityRequest, AvailabilityResponseSchema
from app.services.availability_service import AvailabilityService

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_availability_controller(db: Session = Depends(get_db)) -> GetAvailabilityController:
    service = AvailabilityService(db)
    return GetAvailabilityController(service)

def set_availability_controller(db: Session = Depends(get_db)) -> SetAvailabilityController:
    service = AvailabilityService(db)
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

