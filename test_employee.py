import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(clc):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):  ##### this method will be run everytime before each testing method
        print("setUp")
        self.emp1 = Employee("arash", "fasih", 50000)
        self.emp2 = Employee("fatemeh", "yazdan", 49000)

    def tearDown(self):  ##### this method will be run everytime after each testing method
        print("tearDown")
        pass

    def test_pay_raise(self):
        print("test_pay_raise")
        self.assertEqual(self.emp1.apply_raise(), 52500)
        self.assertEqual(self.emp2.apply_raise(), 51450)

        self.emp1.pay = 30000
        self.emp2.pay = 40000

        self.assertEqual(self.emp1.apply_raise(), 31500)
        self.assertEqual(self.emp2.apply_raise(), 42000)
        print("----------------")

    def test_email(self):
        print("test_email")
        self.assertEqual(self.emp1.email(), "arash.fasih@gmail.com")
        self.assertEqual(self.emp2.email(), "fatemeh.yazdan@gmail.com")
        self.emp1.first = "aryan"
        self.emp2.first = "maryam"

        self.assertEqual(self.emp1.email(), "aryan.fasih@gmail.com")
        self.assertEqual(self.emp2.email(), "maryam.yazdan@gmail.com")
        print("----------------")


    def test_fullname(self):
        print("test_fullname")
        self.assertEqual(self.emp1.fullname(), "arash fasih")
        self.assertEqual(self.emp2.fullname(), "fatemeh yazdan")

        self.emp1.first = "aryan"
        self.emp2.first = "maryam"

        self.assertEqual(self.emp1.fullname(), "aryan fasih")
        self.assertEqual(self.emp2.fullname(), "maryam yazdan")
        print("----------------")




if __name__ == "__main__":
    unittest.main()
