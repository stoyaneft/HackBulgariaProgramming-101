import unittest

from song import Song


class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song(
            'title', 'artist', 'album', 5, 210, 10)

    def test_init_song(self):
        self.assertEqual(self.song.title, 'title')
        self.assertEqual(self.song.artist, 'artist')
        self.assertEqual(self.song.album, 'album')
        self.assertEqual(self.song.rating, 5)
        self.assertEqual(self.song.length, 210)
        self.assertEqual(self.song.bitrate, 10)

    def test_rate(self):
        self.song.rate(4)
        self.assertEqual(self.song.rating, 4)

    def test_rate_throws_exception(self):
        with self.assertRaises(ValueError):
            self.song.rate(6)

if __name__ == '__main__':
    unittest.main()
