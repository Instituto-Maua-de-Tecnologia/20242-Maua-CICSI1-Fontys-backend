from app.schemas.availability import AvailabilityResponseSchema, SetAvailabilityRequest
from app.services.avaialability_services.set_availability_service import SetAvailabilityService
from fastapi import HTTPException, Query


class SetAvailabilityController:

    def __init__(self, service: SetAvailabilityService):
        self.service = service

    def handle(self, data: SetAvailabilityRequest) -> list[AvailabilityResponseSchema]:
        try:
            availability = self.service.set_availability(data.availabilities, data.user_id)

            response_objects = []
            for a in availability:
                response_objects.append(AvailabilityResponseSchema(
                    slot_id=a.slot.slot_id,
                    value=a.value,
                ))

            return response_objects
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Error getting availability: {str(e)}")
