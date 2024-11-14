
from app.core.database import Base, engine
from app.models.users import User
from app.models.type_users import TypeUser
from app.models.subjects import Subject
from app.models.slots import Slot
from app.models.courses import Course
from app.models.semesters import Semester
from app.models.schedules import Schedule
from app.models.coordination import Coordination
from app.models.user_shipping import UserShipping
from app.models.availabilitys import Availability    
from app.models.user_types import UserType
from app.models.user_subjects import UserSubject

if __name__ == "__main__":
    # Criar todas as tabelas no banco de dados
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
