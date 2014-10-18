import unittest

from Fraction import Fraction


class FractionTest(unittest.TestCase):

    def setUp(self):
        self.fraction_a = Fraction(1, 2)
        self.fraction_b = Fraction(2, 3)

    def test_addition(self):
        self.assertEqual(self.fraction_a + self.fraction_b, Fraction(7, 6))

    def test_subtraction(self):
        self.assertEqual(self.fraction_a - self.fraction_b, Fraction(-1, 6))

    def test_fraction_comparison(self):
        self.assertTrue(self.fraction_a < self.fraction_b)
        self.assertFalse(self.fraction_a > self.fraction_b)
        self.assertFalse(self.fraction_a == self.fraction_b)
        self.assertTrue(self.fraction_a == self.fraction_a)

if __name__ == '__main__':
    unittest.main()
