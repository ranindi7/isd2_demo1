from course.course import Course
from department.department import Department

class LectureCourse(Course):
    def __init__(self, name: str, department: Department, credit_hours: int, capacity:int, current_enrollment:int):
        super().__init__(name, department, credit_hours)

        if 