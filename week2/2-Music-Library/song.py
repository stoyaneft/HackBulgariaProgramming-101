class Song:
    MAX_RATING = 5
    MIN_RATING = 0

    def __init__(self, title='', artist='', album='',
                 rating=0, length=0, bitrate=0):
        self.title = title
        self.artist = artist
        self.album = album
        self.rating = rating
        self.length = length
        self.bitrate = bitrate

    def rate(self, rating):
        if Song.MIN_RATING <= rating <= Song.MAX_RATING:
            self.rating = rating
        else:
            raise ValueError
