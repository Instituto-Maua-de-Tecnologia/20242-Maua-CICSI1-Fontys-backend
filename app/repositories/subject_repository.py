from sqlalchemy.orm import Session

from app.domain.entities.user_subject_entity import UserSubjectEntity
from app.models import UserSubject


class SubjectRepository:
    def __init__(self, db: Session):
        self.db = db

    def set_user_subjects(self, user_id: str, subjects: list[str]) -> None:
        user_subjects = self.db.query(UserSubject).filter_by(user_id=user_id).all()
        current_subjects = {s.subject_code for s in user_subjects}

        subject_set = set(subjects)

        to_add = subject_set - current_subjects
        to_remove = current_subjects - subject_set

        records = []
        for s in to_add:
            records.append(UserSubject(user_id=user_id, subject_code=s))

        self.db.add_all(records)

        if to_remove:
            (self.db.query(UserSubject)
             .filter(UserSubject.subject_code.in_(to_remove))
             .delete(synchronize_session=False))

        self.db.commit()
