from sqlalchemy import Column, Integer, String, Enum
from app.db.base import Base
from sqlalchemy.orm import relationship


class Subject(Base):
    __tablename__ = "subjects"

    subject_id = Column(String, primary_key=True, index=True)  # ID único da matéria
    subject_code = Column(String, primary_key=True, index=True)  # Código único da matéria
    name = Column(String(255), nullable=False)
    study_load = Column(Integer, nullable=False)
    
    # Relacionamento com usuários
    users = relationship("UserSubject", back_populates="subject")
