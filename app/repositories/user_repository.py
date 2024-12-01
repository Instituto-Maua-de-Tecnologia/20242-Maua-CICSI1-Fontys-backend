from typing import Optional
from uuid import uuid4
from app.models.type_users import TypeUser
from app.models.user_types import UserType
from sqlalchemy.orm import aliased
from sqlalchemy.orm import Session
from app.models.user_shipping import UserShipping
from app.models.users import User  

from app.domain.interfaces.repositories.user_repository_interface import IUserRepository
from app.domain.entities.user_entity import UserEntity
from app.schemas.user import GetAllProfessorsResponseSchema

class UserRepository(IUserRepository):
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: UserEntity) -> UserEntity:
            db_user = User(
                name=user.name,
                photo=user.photo,
                notes=user.notes,
                microsoft_id=user.microsoft_id
            )
            try:
                self.db.add(db_user)
                self.db.commit()
                self.db.refresh(db_user)
                
                db_type = UserType(
                    user_type_id=str(uuid4()),
                    user_id=db_user.user_id,
                    type_id=4
                )
                self.db.add(db_type)
                self.db.commit()
                self.db.refresh(db_type)
                
            except Exception:
                self.db.rollback()
                raise
            return UserEntity(
                user_id=db_user.user_id,
                microsoft_id=db_user.microsoft_id,
                name=db_user.name,
                photo=db_user.photo,
                notes=db_user.notes
            )
    def get_all_professors(self) -> list[GetAllProfessorsResponseSchema]:
        db_users = (
            self.db.query(
                User.user_id,
                User.name,
                TypeUser.type_name,
                UserShipping.status
            )
            .outerjoin(UserType, User.user_id == UserType.user_id)
            .outerjoin(TypeUser, UserType.type_id == TypeUser.type_id)
            .outerjoin(UserShipping, User.user_id == UserShipping.user_id)
            .filter(TypeUser.type_id == '1')
        )
        return [
            GetAllProfessorsResponseSchema(
                user_id=user_id,
                name=name,
                type_name=type_name,
                status=status,
            )
            for user_id, name, type_name, status in db_users
        ]
