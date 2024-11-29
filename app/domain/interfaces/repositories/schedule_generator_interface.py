from abc import ABC, abstractmethod
from app.schemas.week import Week
from app.domain.entities.schedule_entity import ScheduleEntity

class IScheduleGenerator(ABC):
    @abstractmethod
    def order_schedule(self, list_available_teacher_subject_times, list_of_subjects, semester) -> Week:
        pass