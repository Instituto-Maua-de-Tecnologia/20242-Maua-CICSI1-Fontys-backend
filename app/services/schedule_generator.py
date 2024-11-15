from week import Week
from subject_count import SubjectCount

class ScheduleGenerator:

    def order_schedule(self, list_available_teacher_subject_times, list_of_subjects, semester):
        """
        Takes a list of subjects that need to be taught in a week,
         a list of subject times when professors can teach in that week, and the semester.
         Then it returns a week with the subjects ordered i day's based on the times professors can teach.
        """
        week = Week(semester)

        subjects_sorted = self.sort_list_of_subjects_by_subject_frequency(
            list_available_teacher_subject_times, list_of_subjects)

        for subject in subjects_sorted:
            self.order_days_based_on_amount_of_subjects_per_day(week)
            for day in week.days:
                available_subject_times = list(filter(lambda st: st.subject == subject,
                                                      list_available_teacher_subject_times))
                if self.put_subject_in_day(available_subject_times,day):
                    break
                elif week.days.index(day) == -1:
                    return f"subject: {subject} to the schedule pleas make sure there are enough available times"
                # handel errors better when there is not enough places to put the subjects


        return week

    # noinspection PyMethodMayBeStatic
    def order_days_based_on_amount_of_subjects_per_day(self, week):
        """
        Takes a week and sorts the list of day's in the week based on how many subjects there are taught in that day
        with the least subjects first and the most last.
        """
        week.days.sort(key=lambda x: x.numberOfSubjects)

        return week

    # noinspection PyMethodMayBeStatic
    def sort_list_of_subjects_by_subject_frequency(self, list_available_teacher_subject_times, list_of_subjects):
        """
        Takes a list of timeslots and subjects and returns the list of subjects based on how frequently they appear in the list of timeslots
        giving the least frequent subject first and most frequent last.
        """
        subject_counts = []
        for subject in dict.fromkeys(list_of_subjects):
            if sum(s.subject == subject for s in list_available_teacher_subject_times) != 0:
                subject_counts.append(
                    SubjectCount(sum(s.subject == subject for s in list_available_teacher_subject_times),subject))
            else:
                return "error" # handel error when the list of timeslots does net contain a timeslot for a subject

        for count in subject_counts:
            count.count /= list_of_subjects.count(count.subject_name)

        subject_counts.sort(key=lambda x: x.count)

        sorted_list = []

        for count_subject in subject_counts:
            for subject in filter(lambda s: s == count_subject.subject_name, list_of_subjects):
                sorted_list.append(subject)

        return sorted_list

    # noinspection PyMethodMayBeStatic
    def put_subject_in_day(self, subject_times, target_day):
        """
        Takes a day and a list of subjectTimes when professors can teach a subject, and tries to put the subject in the day.
        When it succeeds it returns true when it fails it returns false.
        """
        try:
            # Filter the SubjectTime instances that match the target day’s weekday
            relevant_subject_times = list(filter(lambda st: st.day == target_day.weekday, subject_times))

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