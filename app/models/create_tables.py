from uuid import uuid4
from app.core.database import Base, engine
from sqlalchemy.orm import sessionmaker
from app.enums.days_of_week_enum import DayOfWeekEnum
from app.enums.time_slot_enum import TimeSlotEnum
from app.enums.type_user_enum import TypeUserEnum
from app.models.courses import Course
from app.models.semesters import Semester
from app.models.slots import Slot
from app.models.subjects import Subject
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
    
    print("Inserting table courses...")
    db_courses = [
        Course(
            course_id=str(uuid4()),
            name="CIC - Computer Science",
            duration="4 years"
        )
    ]
    
    db.add_all(db_courses)
    db.commit()
    
    print("Table courses inserted")
    
    print("Inserting table Subjects...")
    db_subjects = [
        Subject(
            subject_code="TTI101",
            subject_name="Object-Oriented Programming",
        ),
        Subject(
            subject_code="TTI102",
            subject_name="Relational Databases",
        ),
        Subject(
            subject_code="TTI103",
            subject_name="Programming Logic",
        ),
        Subject(
            subject_code="TTI104",
            subject_name="Object-Oriented Modeling",
        ),
        Subject(
            subject_code="TTI105",
            subject_name="Interdisciplinary Integrated Project - Programming",
        ),
        Subject(
            subject_code="TTI106",
            subject_name="User Interface and Experience",
        ),
        Subject(
            subject_code="TTI107",
            subject_name="Front End Development",
        ),
        Subject(
            subject_code="TTI108",
            subject_name="IT Legislation and Ethics",
        ),
        Subject(
            subject_code="TTI109",
            subject_name="Statistics",
        ),
        Subject(
            subject_code="TTI110",
            subject_name="Mathematical Logic and Discrete Mathematics",
        ),
        Subject(
            subject_code="TTI111",
            subject_name="Interdisciplinary Integrated Project - Front End",
        ),
    ]

    db.add_all(db_subjects)
    db.commit()
    
    print("Table subjects inserted")
    
    print("Inserting table semesters...")
    db_semesters = [
        Semester(
            semester_number=1,
            course_id=db_courses[0].course_id,
            subject_code=db_subjects[0].subject_code
        ),
        Semester(
            semester_number=1,
            course_id=db_courses[0].course_id,
            subject_code=db_subjects[1].subject_code
        ),
        Semester(
            semester_number=1,
            course_id=db_courses[0].course_id,
            subject_code=db_subjects[2].subject_code
        ),
        Semester(
            semester_number=1,
            course_id=db_courses[0].course_id,
            subject_code=db_subjects[3].subject_code
        ),
        Semester(
            semester_number=1,
            course_id=db_courses[0].course_id,
            subject_code=db_subjects[4].subject_code
        ),
        Semester(
            semester_number=2,
            course_id=db_courses[0].course_id,
            subject_code=db_subjects[5].subject_code
        ),
        Semester(
            semester_number=2,
            course_id=db_courses[0].course_id,
            subject_code=db_subjects[6].subject_code
        ),
        Semester(
            semester_number=2,
            course_id=db_courses[0].course_id,
            subject_code=db_subjects[7].subject_code
        ),
        Semester(
            semester_number=2,
            course_id=db_courses[0].course_id,
            subject_code=db_subjects[8].subject_code
        ),
        Semester(
            semester_number=2,
            course_id=db_courses[0].course_id,
            subject_code=db_subjects[9].subject_code
        ),
        Semester(
            semester_number=2,
            course_id=db_courses[0].course_id,
            subject_code=db_subjects[10].subject_code
        ),
    ]

    db.add_all(db_semesters)
    db.commit()
    
    print("Table semesters inserted")
    
    print("Finally! uhull :)")