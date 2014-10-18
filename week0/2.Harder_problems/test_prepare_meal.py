import unittest

from prepare_meal import prepare_meal


class PrepareMealTest(unittest.TestCase):

    def test_only_spam(self):
        self.assertEqual(prepare_meal(9), 'spam spam')
        self.assertEqual(prepare_meal(12), 'spam')

    def test_for_empty_string(self):
        self.assertEqual(prepare_meal(4), '')

    def test_only_eggs(self):
        self.assertEqual(prepare_meal(25), 'eggs')

    def test_spam_and_eggs(self):
        self.assertEqual(prepare_meal(45), 'spam spam and eggs')
        self.assertEqual(prepare_meal(27 * 5), 'spam spam spam and eggs')

if __name__ == '__main__':
    unittest.main()
