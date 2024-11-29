from abc import ABC, abstractmethod
from typing import List
from app.domain.entities.user_entity import UserEntity

class IUserRepository(ABC):

    @abstractmethod
    def create_user(self, user: UserEntity) -> UserEntity:
        pass
    
    @abstractmethod
    def get_all_users(self) -> List[UserEntity]:
        pass