from sqlalchemy import Column, String
from app.core.database import Base, engine

class User(Base):
    __tablename__ = "users"

    user_id = Column(String(), primary_key=True, index=True)
    microsoft_id = Column(String(), nullable=False)
    name = Column(String(), nullable=False)
    notes = Column(String(500), nullable=True)

if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)