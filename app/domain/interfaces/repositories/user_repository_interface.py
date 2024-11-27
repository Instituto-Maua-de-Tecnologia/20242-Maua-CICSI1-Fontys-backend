from abc import ABC, abstractmethod
from typing import Optional
from app.domain.entities.user_entity import UserEntity

class IUserRepository(ABC):

    @abstractmethod
    def create_user(self, user: UserEntity) -> UserEntity:
        pass

    @abstractmethod
    def get_by_id(self, user_id: str) -> Optional[UserEntity]:
        pass