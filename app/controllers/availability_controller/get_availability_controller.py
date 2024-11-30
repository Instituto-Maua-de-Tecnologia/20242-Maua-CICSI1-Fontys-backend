from app.schemas.availability import AvailabilityResponseSchema
from app.services.availability_service import AvailabilityService
from fastapi import HTTPException, Query


class GetAvailabilityController:

    def __init__(self, service: AvailabilityService):
        self.service = service

    def handle(self, user_id: str = Query(...)) -> list[AvailabilityResponseSchema]:
        try:
            availability = self.service.get_user_availability(user_id)

            response_objects = []
            for a in availability:
                response_objects.append(AvailabilityResponseSchema(
                    slot_id=a.slot.slot_id,
                    value=a.value,
                ))

            return response_objects
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Error getting availability: {str(e)}")
