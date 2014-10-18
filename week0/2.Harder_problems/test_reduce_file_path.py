import unittest

from reduce_file_path import reduce_file_path


class ReduceFilePathTest(unittest.TestCase):

    def test_staying_in_same_directory(self):
        self.assertEqual(reduce_file_path('/file1//file2/./file3'),
                         '/file1/file2/file3')

    def test_going_back_one_dir(self):
        self.assertEqual(reduce_file_path('/file1/file2/..'), '/file1')
        self.assertEqual(reduce_file_path("/etc/../etc/../etc/../"), '/')

    def test_remove_last_backslash(self):
        self.assertEqual(reduce_file_path('/file1/1/'), '/file1/1')

    def test_remove_every_extra_backslash(self):
        self.assertEqual(reduce_file_path('//////////////'), '/')


if __name__ == '__main__':
    unittest.main()
