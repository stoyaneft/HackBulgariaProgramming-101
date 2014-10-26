import json
from song import Song


class Playlist:

    def __init__(self, name):
        self.name = name
        self.songs = []

    def __str__(self):
        all_songs_info = []
        for song in self.songs:
            length_mins = song.length // 60
            length_secs = song.length % 60
            time_in_mins = '{:02d}:{:02d}'.format(length_mins, length_secs)
            song_info = " ".join([song.artist, song.title, '-', time_in_mins])
            all_songs_info.append(song_info)
        return "\n".join(all_songs_info)

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song_name):
        for song in self.songs:
            if song.title == song_name:
                self.songs.remove(song)
                self.remove_song(song_name)

    def total_length(self):
        total_len = 0
        for song in self.songs:
            total_len += song.length
        return total_len

    def remove_disrated(self, rating):
        for song in self.songs:
            if song.rating < rating:
                self.songs.remove(song)
                self.remove_disrated(rating)

    def remove_bad_quality(self, bitrate_limit):
        for song in self.songs:
            if song.bitrate < bitrate_limit:
                self.songs.remove(song)
                self.remove_bad_quality(bitrate_limit)

    def show_artists(self):
        artists = set()
        for song in self.songs:
            artists.add(song.artist)
        return list(artists)

    def save(self, filename):
        save_data = {'name': self.name, 'songs': []}
        for song in self.songs:
            save_data['songs'].append(song.__dict__)
        with open(filename, 'w') as save_file:
            json.dump(
                save_data, save_file,
                indent=4, separators=(',', ':'), sort_keys=True)

    @staticmethod
    def load(filename):
        with open(filename, 'r') as load_file:
            load_data = json.load(load_file)
        loaded_playlist = Playlist(load_data['name'])
        for song_data in load_data['songs']:
            song = Song(**song_data)
            loaded_playlist.add_song(song)
        return loaded_playlist
