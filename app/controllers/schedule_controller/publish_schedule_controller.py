from fastapi import HTTPException
from app.domain.entities.schedule_entity import ScheduleEntity
from app.schemas.schedule import ScheduleEntitySchemaRequest
from app.services.schedule_services.publish_schedule_service import PublishScheduleService

class PublishScheduleController:
    def __init__(self, schedule_service: PublishScheduleService):
        self.schedule_service = schedule_service

    def handle(self, schedules: list[ScheduleEntitySchemaRequest]) -> dict:
        try:
            print('COMECOU O PARSE DA REQ NO CONTROLLER')
            schedule_entities = [
                ScheduleEntity(
                    user_id=schedule.user_id,
                    slot_id=schedule.slot_id,
                    subject_code=schedule.subject_code,
                    semester_number=schedule.semester_number,
                    course_id=schedule.course_id,
                )
                for schedule in schedules
            ]

            print('passou do parse')

            message = self.schedule_service.execute(schedule_entities)
            return {"message": message}
        except RuntimeError as e:
            raise HTTPException(status_code=500, detail=str(e))
