from typing import List

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.controllers.availability_controller.get_availability_controller import GetAvailabilityController
from app.controllers.availability_controller.set_availability_controller import SetAvailabilityController
from app.controllers.availability_controller.update_availability_controller import UpdateAvailabilityController
from app.core.database import SessionLocal
from app.schemas.availability import  SetAvailabilityRequest, AvailabilityResponseSchema, UpdateAvailabilityRequest, UpdateAvailabilityResponse
from app.services.avaialability_services.set_availability_service import SetAvailabilityService
from app.services.avaialability_services.get_user_availability_service import GetUserAvailabilityService
from app.services.subject_services.set_subject_service import SetSubjectService
from app.services.user_services.set_notes_service import SetNotesService

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
    avail_service = SetAvailabilityService(db)
    notes_service = SetNotesService(db)
    subject_service = SetSubjectService(db)
    return SetAvailabilityController(avail_service, notes_service, subject_service)

@router.get("/availability/", response_model=List[AvailabilityResponseSchema], status_code=200)
def get_availability(
        user_id: str = Query(...),
        controller: GetAvailabilityController = Depends(get_availability_controller)
) -> List[AvailabilityResponseSchema]:
    return controller.handle(user_id)

@router.post("/availability/", response_model=List[AvailabilityResponseSchema], status_code=201)
def set_availability(
        data: SetAvailabilityRequest,
        controller: SetAvailabilityController = Depends(set_availability_controller)
) -> List[AvailabilityResponseSchema]:
    return controller.handle(data)

@router.put("/availability", response_model=UpdateAvailabilityResponse, status_code=200)
def update_availabilities(
    data: UpdateAvailabilityRequest,
    controller: UpdateAvailabilityController = Depends(get_availability_controller)
):
    return controller.handle(data)


