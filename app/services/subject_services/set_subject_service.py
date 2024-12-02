import string

from sqlalchemy.orm import Session

from app.repositories.subject_repository import SubjectRepository
from app.domain.entities.user_entity import UserEntity

class SetSubjectService:
    def __init__(self, db: Session):
        self.repository = SubjectRepository(db)

    def execute(self, user_id: string, subjects: list[string]) -> UserEntity:
        return self.repository.set_user_subjects(user_id, subjects)
