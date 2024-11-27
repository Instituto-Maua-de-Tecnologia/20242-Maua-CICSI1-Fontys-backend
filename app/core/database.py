from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings


SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL_AIVEN

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()



def get_db():
    db = SessionLocal()  # Cria uma nova sessão
    try:
        yield db  # Fornece a sessão para uso
    finally:
        db.close() 