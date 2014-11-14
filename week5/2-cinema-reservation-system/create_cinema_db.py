from cinema_database import CinemaDatabase


def main():
    cinema_db = CinemaDatabase('cinema.db')
    cinema_db.create_all_tables()
    movies = [
        ('The Hunger Games: Catching Fire', 7.9),
        ('Wreck-It Ralph', 7.8),
        ('Her', 8.3)
    ]
    cinema_db.add_movies(movies)
    projections = [
        (1, '3D', '2014-04-01', '19:10'),
        (1, '2D', '2014-04-01', '19:00'),
        (1, '4DX', '2014-04-02', '21:00'),
        (3, '2D', '2014-04-05', '20:20'),
        (2, '3D', '2014-04-02', '22:00'),
        (2, '2D', '2014-04-02', '19:30')
    ]
    cinema_db.add_projections(projections)
    reservations = [
        ('RadoRado', 1, 2, 1),
        ('RadoRado', 1, 3, 5),
        ('RadoRado', 1, 7, 8),
        ('Ivo', 3, 1, 1),
        ('Ivo', 3, 1, 2),
        ('Mysterious', 5, 2, 3),
        ('Mysterious', 5, 2, 4)
    ]
    cinema_db.add_reservations(reservations)

if __name__ == '__main__':
    main()
