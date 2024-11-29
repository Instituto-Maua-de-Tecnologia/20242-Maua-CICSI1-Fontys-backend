from subject_time import SubjectTime
from app.enums.time_slot_enum import TimeSlot
from app.enums.days_of_week_enum import DayOfWeek

class Day:

    def __init__(self, day_name):
        self.timeslots = [SubjectTime(TimeSlot.FIRST_CLASS, DayOfWeek(day_name)),
                          SubjectTime(TimeSlot.SECOND_CLASS,DayOfWeek(day_name)),
                          SubjectTime(TimeSlot.THIRD_CLASS, DayOfWeek(day_name))]
        self.weekday = day_name
        self.numberOfSubjects = 0