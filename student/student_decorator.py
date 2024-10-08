from student.istudent import iStudent

class StudentDecorator(iStudent):
    def __init__(self, student: iStudent):
        self.__student = student

    @property
    def grade_point_average(self) -> float:
        return self.__grade_point_average
    
    