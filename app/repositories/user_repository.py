from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate

class UserRepository:
    def __init__(self, db: Session):
        self.db = db
        
    @staticmethod
    async def create_or_update_user(user_info: dict, db: Session):
        user = db.query(User).filter(User.microsoft_id == user_info["id"]).first()
        if not user:
            user = User(
                microsoft_id=user_info["id"],
                email=user_info["userPrincipalName"],
                name=user_info["displayName"]
            )
            db.add(user)
        else:
            user.name = user_info["displayName"]
            user.email = user_info["userPrincipalName"]
        
        db.commit()
        return user
    