import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.one_employee = Employee('jack', 'tk', 12000)

    def test_give_default_raise(self):
        self.one_employee.give_raise()
        self.assertEqual(12000 + 5000, self.one_employee.money)

    def test_give_custom_raise(self):
        self.one_employee.give_raise(2000)
        self.assertEqual(12000 + 2000, self.one_employee.money)


unittest.main()
