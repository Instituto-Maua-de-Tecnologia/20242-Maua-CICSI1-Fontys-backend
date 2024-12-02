from uuid import uuid4
from app.core.database import Base, engine
from sqlalchemy.orm import sessionmaker
from app.enums.days_of_week_enum import DayOfWeekEnum
from app.enums.time_slot_enum import TimeSlotEnum
from app.enums.type_user_enum import TypeUserEnum
from app.models.courses import Course
from app.models.slots import Slot
from app.models.type_users import TypeUser

if __name__ == "__main__":
    
    print("Dropping all tables...")
    Base.metadata.drop_all(bind=engine)  

    
    print("Creating all tables...")
    Base.metadata.create_all(bind=engine)
    
    print("creating session...")
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    print("Session created")
    
    print("Inserting Table slots...")
    db_slots = []
    i = 1
    for day in DayOfWeekEnum:
        for time in TimeSlotEnum:
            slot = Slot(
                slot_id=i,
                day_of_week=day,
                time=time
            )
            db_slots.append(slot)
            i += 1
    
    db.add_all(db_slots)
    db.commit()
    
    print("Table slot inserted")
    
    print("Inserting table Types...")
    db_types = [
        TypeUser(
            type_id=1,
            type_name=TypeUserEnum.PROFESSOR
        ),
        TypeUser(
            type_id=2,
            type_name=TypeUserEnum.SECRETARY
        ),
        TypeUser(
            type_id=3,
            type_name=TypeUserEnum.COORDINATOR
        ),
        TypeUser(
            type_id=4,
            type_name=TypeUserEnum.NOT_REGISTERED
        )
    ]
    
    db.add_all(db_types)
    db.commit()
    
    print("Table types inserted")
    
    print("Finally! uhull :)")