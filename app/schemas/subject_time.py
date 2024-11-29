from app.enums.days_of_week_enum import DayOfWeek

class SubjectTime:

    def __init__(self, time_slot, day):
        self.subject = None
        self.professor = None
        self.time = time_slot
        self.day = DayOfWeek(day)

    def set_subject_info(self, subject, professor):
        self.subject = subject
        self.professor = professor