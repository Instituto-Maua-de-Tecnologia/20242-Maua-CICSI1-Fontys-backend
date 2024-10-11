from app.db.session import engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def create_tables():
    Base.metadata.create_all(bind=engine)