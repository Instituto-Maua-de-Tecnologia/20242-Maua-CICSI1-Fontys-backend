from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.domain.entities.user import UserEntity

class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def register_user(self, user_data: UserEntity):
        return self.repository.create_user(user_data)