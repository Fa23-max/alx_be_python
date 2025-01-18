import unittest
from simple_calculator import SimpleCalculator

class TestCalculator(unittest.TestCase):
  def test_addition(self):
    self.assertEqual(SimpleCalculator().add(3,2),5,"3 plus 2  expected 5")
    self.assertEqual(SimpleCalculator().add(2, 3), 5)
    self.assertEqual(SimpleCalculator().add(-1, 1), 0)
  def test_subtraction(self):
    self.assertEqual(SimpleCalculator().subtract(3,2),1,"3 subtract 2 expected 1")
  def test_multiplication(self):
    self.assertEqual(SimpleCalculator().multiply(3,2),6,"3 multiply 2 expected 6")
  def test_division(self):
    self.assertEqual(SimpleCalculator().divide(6,3),2,"6 divide 3 expected 2")