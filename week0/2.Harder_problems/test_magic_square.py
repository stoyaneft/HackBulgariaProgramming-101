import unittest

from magic_square import magic_square


class MagicSquareTest(unittest.TestCase):

    def test_magic_square1x1(self):
        self.assertTrue(magic_square([[32]]))

    def test_magic_square2x2(self):
        self.assertTrue(magic_square([[1, 1], [1, 1]]))
        self.assertFalse(magic_square([[1, 2], [1, 1]]))

    def test_magic_square3x3(self):
        self.assertTrue(
            magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]]))
        self.assertFalse(
            magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]]))

    def test_magic_square4x4(self):
        self.assertTrue(
            magic_square([[7, 12, 1, 14], [2, 13, 8, 11],
                          [16, 3, 10, 5], [9, 6, 15, 4]]))


if __name__ == '__main__':
    unittest.main()
