from fastapi import HTTPException
from app.services.schedule_services.get_schedule_by_id import GetScheduleByIdService


class GetScheduleByIdController:
    def __init__(self, service: GetScheduleByIdService):
        self.service = service

    def handle(self, schedule_id: str) -> dict:
        try:
            schedule = self.service.execute(schedule_id)
            return {
                "schedule_id": schedule.schedule_id,
                "message": "Schedule generated successfully"
            }
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Error generating schedule: {str(e)}")