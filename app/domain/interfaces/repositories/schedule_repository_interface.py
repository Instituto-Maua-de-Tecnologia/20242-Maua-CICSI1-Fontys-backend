from abc import ABC, abstractmethod
from typing import Optional
from app.domain.entities.schedule_entity import ScheduleEntity

class IScheduleRepository(ABC):
    @abstractmethod
    def upload_schedule(self, ScheduleEntity: str) -> Optional[str]:
        pass

    @abstractmethod
    def get_schedule_by_id(self, id: str) -> ScheduleEntity:
        pass
    
    def create_schedule(self, schedule: ScheduleEntity) -> ScheduleEntity:
        pass