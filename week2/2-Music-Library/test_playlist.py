import unittest

from playlist import Playlist
from song import Song


class TestPlaylist(unittest.TestCase):

    def setUp(self):
        self.playlist = Playlist('My playlist')
        self.song1 = Song('Name1', 'Artist', 'Album', 3, 240, 10)
        self.song2 = Song('Name2', 'Artist', 'Album', 4, 210, 9)
        self.playlist.add_song(self.song1)
        self.playlist.add_song(self.song2)

    def test_init_playlist(self):
        self.assertEqual(self.playlist.name, 'My playlist')

    def test_add_song(self):
        self.assertIn(self.song1, self.playlist.songs)

    def test_remove_song(self):
        self.playlist.remove_song('Name1')
        flag = False
        for song in self.playlist.songs:
            if song.title == 'Name1':
                flag = True
        self.assertFalse(flag)

    def test_total_length(self):
        self.assertEqual(self.playlist.total_length(), 450)

    def test_remove_disrated(self):
        song3 = Song('Name3', 'Artist', 'Album', 2, 210, 9)
        self.playlist.add_song(song3)
        self.playlist.remove_disrated(4)
        no_disrated_songs = True
        for song in self.playlist.songs:
            if song.rating < 4:
                no_disrated_songs = False
                break
        self.assertTrue(no_disrated_songs)

    def test_remove_bad_quality(self):
        self.playlist.remove_bad_quality(10)
        self.assertNotIn(self.song2, self.playlist.songs)

    def test_show_artists(self):
        self.assertEqual(self.playlist.show_artists(), ['Artist'])

    def test__str__(self):
        self.assertEqual(
            str(self.playlist), 'Artist Name1 - 04:00\nArtist Name2 - 03:30')

    def test_save(self):
        self.playlist.save('playlist.json')

    def test_load(self):
        new_playlist = Playlist.load('playlist.json')
        print()
        print(new_playlist)


if __name__ == '__main__':
    unittest.main()
