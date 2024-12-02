from app.schemas.availability import AvailabilityResponseSchema, SetAvailabilityRequest, SetAvailabilityResponse
from app.services.avaialability_services.set_availability_service import SetAvailabilityService
from fastapi import HTTPException, Query

from app.services.subject_services.set_subject_service import SetSubjectService
from app.services.user_services.set_notes_service import SetNotesService


class SetAvailabilityController:

    def __init__(self, setAvailabilityService: SetAvailabilityService, setNotesService: SetNotesService, setSubjectService: SetSubjectService):
        self.availabilityService = setAvailabilityService
        self.notesService = setNotesService
        self.subjectService =  setSubjectService

    def handle(self, data: SetAvailabilityRequest) -> SetAvailabilityResponse:
        try:
            user = self.notesService.execute(data.user_id, data.notes)
            self.subjectService.execute(data.user_id, data.subjects)
            availability = self.availabilityService.set_availability(data.availabilities, data.user_id)
            response_objects = []
            for a in availability:
                response_objects.append(AvailabilityResponseSchema(
                    slot_id=a.slot.slot_id,
                    value=a.value,
                ))
            response = SetAvailabilityResponse(
                availabilities=response_objects,
                notes=user.notes,
                subjects=data.subjects
            )

            return response
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Error getting availability: {str(e)}")
