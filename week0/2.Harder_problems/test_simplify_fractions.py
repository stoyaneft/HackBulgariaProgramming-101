import unittest

from simplify_fraction import simplify_fraction


class SimplifyFractionTest(unittest.TestCase):

    def test_simplified_fraction(self):
        self.assertEqual(simplify_fraction((1, 3)), (1, 3))

    def test_different_fractions(self):
        self.assertEqual(simplify_fraction((10, 20)), (1, 2))
        self.assertEqual(simplify_fraction((63, 462)), (3, 22))
        self.assertEqual(simplify_fraction((3, 3)), (1, 1))

if __name__ == '__main__':
    unittest.main()
