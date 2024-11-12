from app.schemas.day import Day
from app.enum.days_of_week import DayOfWeek

class Week:
    days = [Day(DayOfWeek.MONDAY), Day(DayOfWeek.TUESDAY), Day(DayOfWeek.WEDNESDAY),
            Day(DayOfWeek.THURSDAY), Day(DayOfWeek.FRIDAY)]
    def __init__(self, semester):
        self.semester = semester
