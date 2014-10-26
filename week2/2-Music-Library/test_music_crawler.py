import unittest

from music_crawler import MusicCrawler


class TestMusicCrawler(unittest.TestCase):

    def test_generate_playlist(self):
        mc = MusicCrawler('/home/stoyaneft/Music')
        print()
        print(mc.generate_playlist())

if __name__ == '__main__':
    unittest.main()
