from app.repositories.user_repository import UserRepository
from sqlalchemy.orm import Session

class GetAllUsersService:
    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)

    def execute(self):
        return self.user_repository.get_all_users()