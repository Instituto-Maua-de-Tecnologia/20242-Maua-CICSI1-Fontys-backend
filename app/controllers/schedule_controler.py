from fastapi import APIRouter
from app.services.schedule_generator import ScheduleGenerator
from app.domain.interfaces.repositories.schedule_generator_interface import IScheduleGenerator
import json

ScheduleRouter = APIRouter(prefix="/schedule")

@ScheduleRouter.post("/", )
def post(available_teacher_times, subjects, semester):
    return [
        json.dumps(ScheduleGenerator.order_schedule(available_teacher_times, subjects, semester))
    ]