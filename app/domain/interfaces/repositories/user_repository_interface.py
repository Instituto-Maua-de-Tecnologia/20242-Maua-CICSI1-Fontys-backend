from abc import ABC, abstractmethod
from typing import Optional
from app.domain.entities.user_entity import UserEntity

class IUserRepository(ABC):
    @abstractmethod
    def get_user_by_email(self, email: str) -> Optional[UserEntity]:
        pass

    @abstractmethod
    def create_user(self, user: UserEntity) -> UserEntity:
        pass