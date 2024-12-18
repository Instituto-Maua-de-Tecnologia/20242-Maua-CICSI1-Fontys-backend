from app.schemas.slots import SlotBase
from fastapi import HTTPException
from app.services.slot_services.get_all_slots_service import GetAllSlotsService


class GetAllSlotsController:

    def __init__(self, service: GetAllSlotsService):
        self.service = service

    def handle(self) -> list[SlotBase]:
        try:
            slots = self.service.get_all()
            response_objects = []
            for s in slots:
                response_objects.append(SlotBase(
                    slot_id=s.slot_id,
                    day_of_week=s.day_of_week,
                    time=s.time,
                ))
            return response_objects
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Error getting slots: {str(e)}")
