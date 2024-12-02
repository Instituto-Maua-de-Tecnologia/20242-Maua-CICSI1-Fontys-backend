from fastapi import HTTPException, Depends
from app.schemas.availability import UpdateAvailabilityRequest, UpdateAvailabilityResponse
from app.services.avaialability_services.update_availability_service import AvailabilityService


class UpdateAvailabilityController:
    def __init__(self, service: AvailabilityService):
        self.service = service

    def handle(self, request: UpdateAvailabilityRequest) -> UpdateAvailabilityResponse:
        try:
            return self.service.update_availabilities(
                user_id=request.user_id,
                availabilities=request.availabilities,
                notes=request.notes,
                subject_code=request.subject_code
            )
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))