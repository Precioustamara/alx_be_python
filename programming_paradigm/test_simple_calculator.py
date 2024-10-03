import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Add more assertions to thoroughly test the add method.

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(6, 2), 4)
        self.assertEqual(self.calc.subtract(9, 3), 6)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 5), 10)
        self.assertEqual(self.calc.multiply(3, 3), 9)

    def test_division(self):
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(20, 4), 5)
        with self.assertRaises(ZeroDivisionError):
            self.assertEqual(self.calc.divide(6, 0), 6)


# Remember to write additional test methods for subtract, multiply, and divide.

if __name__ == "__main__": 
    unittest.main()