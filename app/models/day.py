from app.models.subject_time import SubjectTime
from app.enum.time_slot import TimeSlot
from app.enum.days_of_week import DayOfWeek

class Day:

    def __init__(self, day_name):
        self.timeslots = [SubjectTime(TimeSlot.FIRST_CLASS, DayOfWeek(day_name)),
                          SubjectTime(TimeSlot.SECOND_CLASS,DayOfWeek(day_name)),
                          SubjectTime(TimeSlot.THIRD_CLASS, DayOfWeek(day_name))]
        self.weekday = day_name
        self.numberOfSubjects = 0