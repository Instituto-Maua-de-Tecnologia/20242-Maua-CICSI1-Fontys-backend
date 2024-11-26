from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.availability import AvailabilityBase, GetUserAvailabilityRequest
from app.services.availability_service import AvailabilityService

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/availability/", response_model=List[AvailabilityBase])
def get_availability(user_id: str = Query(...), db: Session = Depends(get_db)):
    service = AvailabilityService(db)
    availability = service.get_user_availability(user_id)
    return availability