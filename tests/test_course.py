"""
Description: Unit tests for the Course class.
Author: ACE Faculty
Modified by: {Student Name}
Date: {Date}
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_course.py
"""
import unittest

from course.course import Course
from department.department import Department

class TestClient(unittest.TestCase):
    
    def test_init_valid(self):
        course = Course("Intermediate Software Development", Department.COMPUTER_SCIENCE,6)

        # name mangaling
        self.assertEqual("Intermediate Software Development", course._Course__name)
        self.assertEqual(Department.COMPUTER_SCIENCE, course._Course__department)
        self.assertEqual(6, course._Course__credit_hours)
    

    def test_init_invalid_name_raises_exception(self):
        with self.assertRaises(ValueError):
            course = Course(" ", Department.COMPUTER_SCIENCE, 6)
    
    def test_init_invalid_department_raises_expection(self):
        with self.assertRaises(ValueError):
            course = Course("Intermediate Software Developpmet", None, 6)

    def test_init_invalid_credit_hours_raises_exception(self):
        with self.assertRaises(ValueError):
            course = Course("Intermediate Software Develoment", Department.COMPUTER_SCIENCE, "six")
    
    def setUp(self):
        self.course = Course("Intermediate Software Development", Department.COMPUTER_SCIENCE, 6)

    def test_name_accessor(self):
        self.assertEqual("Intermediate Software Development", self.course.name)
    
    def test_department_accessor(self):
        self.assertEqual(Department.COMPUTER_SCIENCE, self.course.deparment)

    def test_credit_hours_accessor(self):
        self.assertEqual(6, self.course.credit_hours)
    
    def test_str(self):
        expected = ("Course: Intermediate Software Development\n"
                    + "Department: Computer Science\n"
                    + "Credit Hours: 6")
        self.assertEqual(expected, str(self.course))
