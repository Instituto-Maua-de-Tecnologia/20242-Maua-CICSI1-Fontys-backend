from day import Day
from app.enums.days_of_week_enum import DayOfWeekEnum

class Week:
    days = [Day(DayOfWeekEnum.MONDAY), Day(DayOfWeekEnum.TUESDAY), Day(DayOfWeekEnum.WEDNESDAY),
            Day(DayOfWeekEnum.THURSDAY), Day(DayOfWeekEnum.FRIDAY)]
    def __init__(self, semester):
        self.semester = semester
