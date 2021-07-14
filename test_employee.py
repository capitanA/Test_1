import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp1 = Employee("arash", "fasih", 50000)
        self.emp2 = Employee("fatemeh", "yazdan", 49000)

    def tearDown(self):
        pass

    def test_pay_raise(self):
        self.assertEqual(self.emp1.apply_raise(), 52500)
        self.assertEqual(self.emp2.apply_raise(), 51450)

        self.emp1.pay = 30000
        self.emp2.pay = 40000

        self.assertEqual(self.emp1.apply_raise(), 31500)
        self.assertEqual(self.emp2.apply_raise(), 42000)

    def test_email(self):
        self.assertEqual(self.emp1.email(), "arash.fasih@gmail.com")
        self.assertEqual(self.emp2.email(), "fatemeh.yazdan@gmail.com")
        self.emp1.first = "aryan"
        self.emp2.first = "maryam"

        self.assertEqual(self.emp1.email(), "aryan.fasih@gmail.com")
        self.assertEqual(self.emp2.email(), "maryam.yazdan@gmail.com")

    def test_fullname(self):
        self.assertEqual(self.emp1.fullname(), "arash fasih")
        self.assertEqual(self.emp2.fullname(), "fatemeh yazdan")

        self.emp1.first = "aryan"
        self.emp2.first = "maryam"

        self.assertEqual(self.emp1.fullname(), "aryan fasih")
        self.assertEqual(self.emp2.fullname(), "maryam yazdan")


if __name__ == "__main__":
    unittest.main()
