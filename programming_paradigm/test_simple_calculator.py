import unittest
from simple_calculator import SimpleCalculator

class TestCalculator(unittest.TestCase):

  def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

  def test_addition(self):
    self.assertEqual(self.calc.add(3,2),5,"3 plus 2  expected 5")
    self.assertEqual(self.calc.add(2, 3), 5)
    self.assertEqual(self.calc.add(-1, 1), 0)
  def test_subtraction(self):
    self.assertEqual(self.calc.subtract(3,2),1,"3 subtract 2 expected 1")
  def test_multiplication(self):
    self.assertEqual(self.calc.multiply(3,2),6,"3 multiply 2 expected 6")
  def test_division(self):
    self.assertEqual(self.calc.divide(6,3),2,"6 divide 3 expected 2")
    self.assertEqual(self.calc.divide(3,0,None,"3 divide 0 expected None"))