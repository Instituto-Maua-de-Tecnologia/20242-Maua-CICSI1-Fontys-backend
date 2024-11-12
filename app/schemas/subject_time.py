from app.enum.days_of_week import DayOfWeek

class SubjectTime:

    def __init__(self, time_slot, day):
        self.subject = None
        self.professor = None
        self.time = time_slot
        self.day = day

    def set_subject_info(self, subject, professor):
        self.subject = subject
        self.professor = professor