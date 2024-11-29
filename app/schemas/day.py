from subject_time import SubjectTime
from app.enums.time_slot_enum import TimeSlotEnum
from app.enums.days_of_week_enum import DayOfWeekEnum

class Day:

    def __init__(self, day_name):
        self.timeslots = [SubjectTime(TimeSlotEnum.FIRST_CLASS, DayOfWeekEnum(day_name)),
                          SubjectTime(TimeSlotEnum.SECOND_CLASS,DayOfWeekEnum(day_name)),
                          SubjectTime(TimeSlotEnum.THIRD_CLASS, DayOfWeekEnum(day_name))]
        self.weekday = day_name
        self.numberOfSubjects = 0