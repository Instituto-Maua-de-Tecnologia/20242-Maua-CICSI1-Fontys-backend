from app.models.day import day
from app.enum.days_of_week import DayOfWeek

class Week:
    days = [day(DayOfWeek.MONDAY), day(DayOfWeek.TUESDAY), day(DayOfWeek.WEDNESDAY),
            day(DayOfWeek.THURSDAY), day(DayOfWeek.FRIDAY)]
    def __init__(self, semester):
        self.semester = semester
