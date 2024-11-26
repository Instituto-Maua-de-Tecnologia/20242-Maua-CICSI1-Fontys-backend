from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.user import UserBase, UserInDB
from app.services.user_service import UserService
from app.domain.entities.user_entity import UserEntity

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/", response_model=UserInDB)
def create_user(user: UserBase, db: Session = Depends(get_db)):
    service = UserService(db)
    user_entity = UserEntity(name=user.name, photo=user.photo, notes=user.notes)
    db_user = service.register_user(user_entity)
    if not db_user:
        raise HTTPException(status_code=400, detail="User already exists")
    return db_user

@router.get('/health')
def health():
    return {'status': 'ok'}