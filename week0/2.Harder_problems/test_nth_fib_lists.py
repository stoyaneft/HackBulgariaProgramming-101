import unittest

from nth_fib_lists import nth_fib_lists


class NthFibListsTest(unittest.TestCase):

    def test_1st_fib_list(self):
        self.assertEqual(nth_fib_lists([1], [2], 1), [1])

    def test_fib_list_with_empty_list(self):
        self.assertEqual(nth_fib_lists([], [1, 2], 4), [1, 2, 1, 2])

    def test_fib_list_with_2empty_lists(self):
        self.assertEqual(nth_fib_lists([], [], 20), [])

    def test_normal_nth_fib(self):
        self.assertEqual(nth_fib_lists([1, 2], [1, 3], 3), [1, 2, 1, 3])


if __name__ == '__main__':
    unittest.main()
