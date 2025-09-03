from datetime import datetime

class Student:
    def __init__(self, name):
        self.name = name
        self._enrollments = []
        self._grades = {}

    def enroll(self, course):
        enrollment = Enrollment(self, course)
        self._enrollments.append(enrollment)
        course.add_enrollment(enrollment)

    def course_count(self):
        return len(self._enrollments)

    def aggregate_average_grade(self):
        total_grades = sum(self._grades.values())
        num_courses = len(self._grades)
        return total_grades / num_courses

class Course:
    def __init__(self, title):
        self.title = title
        self._enrollments = []

    def add_enrollment(self, enrollment):
        self._enrollments.append(enrollment)

class Enrollment:
    all = []
    
    def __init__(self, student, course):
        self.student = student
        self.course = course
        self._enrollment_date = datetime.now()
        type(self).all.append(self)

    def get_enrollment_date(self):
        return self._enrollment_date

    @classmethod
    def aggregate_enrollments_per_day(cls):
        enrollment_count = {}
        for enrollment in cls.all:
            date = enrollment.get_enrollment_date().date()
            enrollment_count[date] = enrollment_count.get(date, 0) + 1
        return enrollment_count