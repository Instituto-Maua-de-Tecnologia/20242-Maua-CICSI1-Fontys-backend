


from fastapi import HTTPException
from app.schemas.schedule import CreateScheduleIASchema
from app.services.schedule_services.create_schedule_IA_service import CreateScheduleIAService


class CreateScheduleIAController:
    def __init__(self, service: CreateScheduleIAService):
        self.service = service

    def handle(self, data: CreateScheduleIASchema) -> dict:
        try:
            schedule = self.service.generate_schedule(data)
            return {
                "schedule_id": schedule.schedule_id,
                "message": "Schedule generated successfully"
            }
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Error generating schedule: {str(e)}")