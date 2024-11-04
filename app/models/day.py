from app.models.subjectTime import subjectTime
from app.enum.time_slot import TimeSlot

class day:

    def __init__(self, dayName):
        self.timeslots = [subjectTime(TimeSlot.FIRST_CLASS), subjectTime(TimeSlot.SECOND_CLASS),
                          subjectTime(TimeSlot.THIRD_CLASS)]
        self.weekDay = dayName