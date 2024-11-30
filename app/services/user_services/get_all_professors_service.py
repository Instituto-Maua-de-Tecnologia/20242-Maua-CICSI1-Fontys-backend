from app.repositories.user_repository import UserRepository
from sqlalchemy.orm import Session

from app.schemas.user import GetAllProfessorsResponseSchema

class GetAllProfessorsService:
    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)
        
    def execute(self) -> list[GetAllProfessorsResponseSchema]:

        users = self.user_repository.get_all_professors()
        
        return users
        