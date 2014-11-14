import sqlite3


class CinemaDatabase:

    def __init__(self, db_name):
        self.db = sqlite3.connect(db_name)
        self.cursor = self.db.cursor()

    def create_movies_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS movies(
            id INTEGER PRIMARY KEY,
            name TEXT,
            rating REAL
        )''')
        self.db.commit()

    def create_projections_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS projections(
            id INTEGER PRIMARY KEY,
            movie_id INTEGER,
            type TEXT,
            date TEXT,
            time TEXT,
            FOREIGN KEY(movie_id) REFERENCES movies(id)
        )''')
        self.db.commit()

    def create_reservations_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS reservations(
            id INTEGER PRIMARY KEY,
            username TEXT,
            projection_id INTEGER,
            row INTEGER,
            col INTEGER,
            FOREIGN KEY(projection_id) REFERENCES projections(id)
        )''')
        self.db.commit()

    def create_all_tables(self):
        self.create_movies_table()
        self.create_projections_table()
        self.create_reservations_table()

    def add_movies(self, movies):
        self.cursor.executemany('''
    INSERT INTO movies(name, rating) VALUES(?, ?)''', movies)
        self.db.commit()

    def add_projections(self, projections):
        self.cursor.executemany('''
    INSERT INTO projections(movie_id, type, date, time) VALUES(?, ?, ?, ?)''',
                                projections)
        self.db.commit()

    def add_reservations(self, reservations):
        self.cursor.executemany('''
    INSERT INTO reservations(username, projection_id, row, col)
    VALUES(?, ?, ?, ?)''', reservations)
        self.db.commit()
