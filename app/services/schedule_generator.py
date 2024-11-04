from app.models.week import week

class scheduleGenerator:

    def orderSchedule(self, list_available_teacher_subjectTimes, list_of_subjects, semester):
        week.semester = semester

        return week

    def orderDaysBasedOnAmountOfSubjectsPerDay(self, week):
        week.days.sort(key=lambda x: x.numberOfSubjects)