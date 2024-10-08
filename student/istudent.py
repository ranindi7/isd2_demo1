from abc import ABC, abstractmethod

class iStudent(ABC):
    """
    Interface for student
    """

    @abstractmethod
    def grade_point_average(self) -> float:
        pass

    