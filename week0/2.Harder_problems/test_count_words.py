import unittest

from count_words import count_words


class CountWordsTest(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual({}, count_words([]))

    def test_count_words(self):
        self.assertEqual(count_words(["apple", "banana", "apple", "pie"]), {
                         'apple': 2, 'pie': 1, 'banana': 1})
        self.assertEqual(
            count_words(["python", "python", "python", "ruby"]), {
                'ruby': 1, 'python': 3})

if __name__ == '__main__':
    unittest.main()
