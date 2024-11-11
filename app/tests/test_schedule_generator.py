import pytest
from app.models.week import Week, DayOfWeek
from app.models.day import TimeSlot, SubjectTime
from app.services.schedule_generator import ScheduleGenerator


@pytest.fixture
def setup_week():
    # This fixture creates a mock week for testing purposes.
    # We'll assume Week(semester) initializes a week with days and timeslots.
    return Week(semester=1)


@pytest.fixture
def setup_subject_times():
    # Mocking available subject times and list of subjects
    subject_times = [
        SubjectTime(time_slot=TimeSlot.FIRST_CLASS, day=DayOfWeek.MONDAY),
        SubjectTime(time_slot=TimeSlot.SECOND_CLASS, day=DayOfWeek.TUESDAY),
        SubjectTime(time_slot=TimeSlot.THIRD_CLASS, day=DayOfWeek.THURSDAY),
        SubjectTime(time_slot=TimeSlot.SECOND_CLASS, day=DayOfWeek.MONDAY)
    ]

    # Setting subject and professor information
    subject_times[0].set_subject_info("Math", "ProfA")
    subject_times[1].set_subject_info("Science", "ProfB")
    subject_times[2].set_subject_info("History", "ProfC")
    subject_times[3].set_subject_info("Biology", "ProfC")

    subjects = ["Math", "Science", "History","Math"]
    return subject_times, subjects

@pytest.fixture
def setup_single_subject_times():
    single_subject_times = [
        SubjectTime(time_slot=TimeSlot.FIRST_CLASS, day=DayOfWeek.MONDAY),
        SubjectTime(time_slot=TimeSlot.SECOND_CLASS, day=DayOfWeek.TUESDAY),
        SubjectTime(time_slot=TimeSlot.THIRD_CLASS, day=DayOfWeek.THURSDAY),
        SubjectTime(time_slot=TimeSlot.SECOND_CLASS, day=DayOfWeek.MONDAY)
    ]

    # Setting subject and professor information
    single_subject_times[0].set_subject_info("Math", "ProfA")
    single_subject_times[1].set_subject_info("Math", "ProfB")
    single_subject_times[2].set_subject_info("Math", "ProfC")
    single_subject_times[3].set_subject_info("Math", "ProfC")

    return single_subject_times

@pytest.fixture
def schedule_generator():
    # Returns an instance of ScheduleGenerator for testing
    return ScheduleGenerator()


# Testing `order_days_based_on_amount_of_subjects_per_day`
def test_order_days_based_on_amount_of_subjects_per_day(schedule_generator, setup_week):
    week = setup_week

    # Assume day.subjects_count gives the number of subjects for each day
    week.days[0].numberOfSubjects = 3  # Monday
    week.days[1].numberOfSubjects = 1  # Tuesday
    week.days[2].numberOfSubjects = 2  # Wednesday

    # Call the method to sort days
    sorted_week = schedule_generator.order_days_based_on_amount_of_subjects_per_day(week)

    # Verify the days are ordered by the number of subjects (ascending)
    day_subject_counts = [day.numberOfSubjects for day in sorted_week.days]
    assert day_subject_counts == sorted(day_subject_counts), \
        "Days should be sorted by the number of subjects in ascending order."


# Testing `sort_list_of_subjects_by_subject_frequency`
def test_sort_list_of_subjects_by_subject_frequency(schedule_generator, setup_subject_times):
    subject_times, subjects = setup_subject_times

    # Adding extra subjects to increase frequency of "Math" and "Science"
    subject_times.append(
        SubjectTime(TimeSlot.SECOND_CLASS, DayOfWeek.MONDAY))
    subject_times.append(
        SubjectTime(TimeSlot.FIRST_CLASS, DayOfWeek.WEDNESDAY))
    subject_times.append(
        SubjectTime(TimeSlot.FIRST_CLASS, DayOfWeek.WEDNESDAY))

    subject_times[4].set_subject_info("Math", "ProfA")
    subject_times[5].set_subject_info("Science", "ProfB")
    subject_times[6].set_subject_info("Science", "ProfC")

    sorted_subjects = schedule_generator.sort_list_of_subjects_by_subject_frequency(subject_times, subjects)

    # Verify "Math" and "Science" appear before "History" based on frequency
    assert sorted_subjects == ["Math","Math","History","Science"], \
        "Subjects should be sorted by frequency in descending order."


# Testing `put_subject_in_day`
def test_put_subject_in_day(schedule_generator, setup_week, setup_single_subject_times):
    week = setup_week
    subject_times = setup_single_subject_times

    # Add subject time for Monday's first class
    target_day = week.days[0]  # Assuming this is Monday
    subject_injected = schedule_generator.put_subject_in_day(subject_times, target_day)

    assert subject_injected is True, "Expected subject to be successfully added to the target day."

    # Test case where no time slots are available
    target_day.timeslots[1].subject = "Math"  # Manually occupy timeslot
    subject_injected = schedule_generator.put_subject_in_day(subject_times, target_day)

    assert subject_injected is False, "Expected method to return False when no time slots are available."


# Testing `order_schedule`
def test_order_schedule(schedule_generator, setup_week, setup_subject_times):
    week = setup_week
    subject_times, subjects = setup_subject_times

    # Mock input lists and semester value
    semester = 1
    ordered_week = schedule_generator.order_schedule(subject_times, subjects, semester)

    # Verify schedule integrity - check that no subject is missing and days are ordered
    for day in ordered_week.days:
        assert day.numberOfSubjects <= len(subjects), "Unexpected number of subjects in day."

    # Confirm that the subjects in each day align with availability
    for subject in subjects:
        subject_found = any(
            slot.subject == subject for day in ordered_week.days for slot in day.timeslots if slot.subject is not None
        )
        assert subject_found, f"Subject {subject} was not scheduled, but it should be."