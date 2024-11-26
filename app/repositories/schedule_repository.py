from sqlalchemy.orm import Session
from app.models.users import User  # Modelo do banco de dados
from app.domain.interfaces.repositories.schedule_repository_interface import IScheduleRepository
from app.domain.entities.user_entity import UserEntity  # Entidade de domínio

class ScheduleRepository(IScheduleRepository):
    def __init__(self, db: Session):
        self.db = db

    def upload_schedule(self, user_id: str) -> UserEntity:
        db_user = self.db.query(User).filter(User.user_id == user_id).first()
        if db_user:
            return UserEntity(
                id=db_user.user_id,
                name=db_user.name,
                photo=db_user.photo,
                notes=db_user.notes
            )
        return None

    def get_schedule_by_id(self, user: UserEntity) -> UserEntity:
        db_user = User(
            name=user.name,
            photo=user.photo,
            notes=user.notes
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return UserEntity(
            id=db_user.user_id,
            name=db_user.name,
            photo=db_user.photo,
            notes=db_user.notes
        )