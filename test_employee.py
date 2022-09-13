import unittest
from employee import Employee
from unittest.mock import patch


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUp(self):
        print("setUp called")
        self.emp_1 = Employee('John', 'Smith', 50000)
        self.emp_2 = Employee('Jane', 'Doe', 60000)

    @classmethod
    def tearDown(self):
        print("tearDown called")

    def test_email(self):
        print("test_email")
        self.assertEqual(self.emp_1.email, 'John.Smith@company.com')
        self.assertEqual(self.emp_2.email, 'Jane.Doe@company.com')

    def test_fullname(self):
        print("test_fullname")
        self.assertEqual(self.emp_1.fullname, 'John Smith')
        self.assertEqual(self.emp_2.fullname, 'Jane Doe')

    def test_pay(self):
        print("test_pay")
        self.assertEqual(self.emp_1.pay, 50000)
        self.assertEqual(self.emp_2.pay, 60000)

