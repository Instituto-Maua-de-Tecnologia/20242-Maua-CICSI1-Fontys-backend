from fastapi import HTTPException
from app.enums.availability_values_enum import AvailabilityValuesEnum
from app.enums.days_of_week_enum import DayOfWeekEnum
from app.enums.time_slot_enum import TimeSlotEnum
from app.schemas.schedule import GenerateScheduleSchema
from app.services.schedule_services.generate_schedule_service import GenerateScheduleService


class GenerateScheduleController:
    def __init__ (self, schedule_service: GenerateScheduleService):
        self.schedule_service = schedule_service

    def handle(self):
        try:

            schedules = self.schedule_service.execute()

            response = []
            for schedule in schedules:
                response.append(GenerateScheduleSchema(
                    user_id=schedule.get('user_id'),
                    name=schedule.get('name'),
                    subject_code=schedule.get('subject_code'),
                    slot_id=schedule.get('slot_id'),
                    day_of_week=DayOfWeekEnum[schedule.get('day_of_week')],
                    time=TimeSlotEnum[schedule.get('time')],
                    availability_value=AvailabilityValuesEnum[schedule.get('availability_value')],
                    subject_name=schedule.get('subject_name'),
                    course_id=schedule.get('course_id'),
                    semester_number=schedule.get('semester_number')
                ))
            return response

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error generating schedule: {str(e)}")