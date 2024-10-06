import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        # Regular cases
        self.assertEqual(self.calc.add(2,3),5)
        self.assertEqual(self.calc.add(-1,1),0)
        self.assertEqual(self.calc.add(0,0),0)
        # Edge case: large numbers
        self.assertEqual(self.calc.add(1000000,1000000),2000000)

    def test_subtraction(self):
        """Test the subtraction method."""
        # Regular cases
        self.assertEqual(self.calc.subtract(5,3),2)
        self.assertEqual(self.calc.subtract(-1,-1),0)
        self.assertEqual(self.calc.subtract(0,0),0)
        # Edge case: negative result
        self.assertEqual(self.calc.subtract(3,5),-2)

    def test_multiplication(self):
        """Test the multiplication method."""
        # Regular cases
        self.assertEqual(self.calc.multiply(2,3),6)
        self.assertEqual(self.calc.multiply(-1,1),-1)
        self.assertEqual(self.calc.multiply(0,1000),0)
        # Edge case: large numbers
        self.assertEqual(self.calc.multiply(100000,100000),10000000000)

    def test_division(self):
        """Test the division method."""
        # Regular cases
        self.assertEqual(self.calc.divide(10,2),5)
        self.assertEqual(self.calc.divide(9,3),3)
        self.assertEqual(self.calc.divide(-9,3),-3)
        # Edge case: division by zero
        self.assertIsNone(self.calc.divide(10,0))
        # Edge case: floating point result
        self.assertAlmostEqual(self.calc.divide(10,3),3.33333333,places=7)

if __name__ == '__main__':
    unittest.main()
