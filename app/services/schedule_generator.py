from app.models.week import Week

class ScheduleGenerator:

    def order_schedule(self, list_available_teacher_subject_times, list_of_subjects, semester):
        Week(semester)

        subjects_sorted = self.sort_list_of_subjects_by_subject_frequency(
            list_available_teacher_subject_times, list_of_subjects)

        for subject in subjects_sorted:
            self.order_days_based_on_amount_of_subjects_per_day(Week)
            for day in Week.days:
                available_subject_times = filter(lambda st: st.subjectTime.subject == subject, subjects_sorted)
                if self.put_subject_in_day(available_subject_times,day):
                    break
                elif Week.days.index(day) == -1:
                    return f"subject: {subject} to the schedule pleas make sure there are enough available times"


        return Week

    # noinspection PyMethodMayBeStatic
    def order_days_based_on_amount_of_subjects_per_day(self, week):
        """
        Takes a week and sorts the list of day's in the week based on how many subjects there are taught in that day
        with the least subjects first and the most last.
        """
        week.days.sort(key=lambda x: x.numberOfSubjects)

    # noinspection PyMethodMayBeStatic
    def sort_list_of_subjects_by_subject_frequency(self, list_available_teacher_subject_times, list_of_subjects):
        """
        Takes a list of timeslots and subjects and returns a list of subjects that are in the timeslots and in the given
        list of subjects, sorted based on frequency giving the least frequent subject first and most frequent last.
        """
        available_teacher_subjects = []
        for subject in set(list_available_teacher_subject_times):
            if subject in list_of_subjects:
                available_teacher_subjects.append((list_available_teacher_subject_times.count(subject), subject))

        available_teacher_subjects.sort(key=lambda tup: (-tup[0], tup[1]))
        return available_teacher_subjects

    # noinspection PyMethodMayBeStatic
    def put_subject_in_day(self, subject_times, target_day):
        """
        Takes a day and a list of subjectTimes when professors can teach a subject, and tries to put the subject in the day.
        When it succeeds it returns true when it fails it returns false.
        """
        try:
            # Filter the SubjectTime instances that match the target day’s weekday
            relevant_subject_times = filter(lambda st: st.day.weekday == target_day.weekday, subject_times)

            # Find an available timeslot in the target day
            for subject_time in relevant_subject_times:
                for day_timeslot in target_day.timeslots:
                    if day_timeslot.time == subject_time.time and day_timeslot.subject is None:
                        day_timeslot.set_subject_info(subject_time.subject, subject_time.professor)
                        day_timeslot.numberOfSubjects =+ 1
                        return True  # Subject assigned successfully
            return False  # No available timeslot found for the subject
        except AttributeError:
            # Handling cases where target_day or subject_times lack expected attributes
            return False