import unittest

from is_an_bn import is_an_bn


class IsAnBnTest(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(is_an_bn(''))

    def test_non_anbn_str(self):
        self.assertFalse(is_an_bn('grisho'))
        self.assertFalse(is_an_bn('bbaa'))
        self.assertFalse(is_an_bn('aab'))

    def test_anbn_words(self):
        self.assertTrue(is_an_bn('aaabbb'))
        self.assertTrue(('aabb'))

if __name__ == '__main__':
    unittest.main()
