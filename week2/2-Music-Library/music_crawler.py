from os import listdir
from os.path import join

import mutagen
from mutagen.mp3 import MP3

from playlist import Playlist
from song import Song


class MusicCrawler:

    def __init__(self, directory_path):
        self.directory_path = directory_path

    def generate_playlist(self):
        playlist = Playlist('playlist for' + self.directory_path)
        for f in listdir(self.directory_path):
            full_filepath = join(self.directory_path, f)
            if mutagen.File(full_filepath, options=[MP3]):
                metadata = mutagen.File(full_filepath, easy=True)
                song_data = {}
                song_data['title'] = metadata['title'][0]
                song_data['artist'] = metadata['artist'][0]
                song_data['album'] = metadata['album'][0]
                song_data['length'] = int(metadata.info.length)
                song_data['bitrate'] = metadata.info.bitrate
                song = Song(**song_data)
                playlist.add_song(song)
        return playlist
