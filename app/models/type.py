

from sqlalchemy import Column, String


class Type:
    __tablename__ = "type"
    
    type_id = Column(String, primary_key=True, index=True)
    type_name = Column(String, nullable=False)
        