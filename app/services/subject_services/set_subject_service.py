import string

from sqlalchemy.orm import Session

from app.repositories.subject_repository import SubjectRepository

class SetSubjectService:
    def __init__(self, db: Session):
        self.repository = SubjectRepository(db)

    def execute(self, user_id: string, subjects: list[string]) -> None:
        return self.repository.set_user_subjects(user_id, subjects)
