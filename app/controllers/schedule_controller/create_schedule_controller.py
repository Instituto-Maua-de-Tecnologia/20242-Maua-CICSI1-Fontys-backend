from fastapi import HTTPException
from app.schemas.schedule import CreateScheduleSchema
from app.services.schedule_services.create_schedule_service import CreateScheduleService


class CreateScheduleController:
    def __init__(self, service: CreateScheduleService):
        self.service = service

    def create_schedule(self, data: CreateScheduleSchema) -> dict:
        try: 
            schedule = self.service.execute(
                course_id=data.course_id,
                user_id=data.user_id,
                slot_id=data.slot_id,
                subject_code=data.subject_code,
                semester_number=data.semester_number,
                created_at=data.created_at
            )
            return {
                "schedule_id": schedule.schedule_id,
                "message": "Schedule created successfully"
            }
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Error creating schedule: {str(e)}")