import string

from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.domain.entities.user_entity import UserEntity

class SetNotesService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def execute(self, user_id: string, notes: string) -> UserEntity:
        return self.repository.set_user_notes(user_id, notes)
