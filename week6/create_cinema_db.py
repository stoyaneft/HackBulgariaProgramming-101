from cinema import Cinema


def create_cinema_db():
    cinema = Cinema(10, 10)
    movies = [
        {"name": 'The Hunger Games: Catching Fire',
         "rating": 7.9},
        {'name': 'Wreck-It Ralph',
         'rating': 7.8},
        {'name': 'Her',
         'rating': 8.3}
    ]

    projections = [
        {'movie_id': 1, 'type': '3D',
            'date': '2014-04-01', 'time': '19:10'},
        {'movie_id': 1, 'type': '2D',
            'date': '2014-04-01', 'time': '19:00'},
        {'movie_id': 1, 'type': '4DX',
            'date': '2014-04-02', 'time': '21:00'},
        {'movie_id': 3, 'type': '2D',
         'date': '2014-04-05', 'time': '20:20'},
        {'movie_id': 2, 'type': '3D',
            'date': '2014-04-02', 'time': '22:00'},
        {'movie_id': 2, 'type': '2D',
         'date': '2014-04-02', 'time': '19:30'}
    ]

    reservations = [
        {'username': 'RadoRado', 'projection_id': 1,
         'row': 2, 'col': 1},
        {'username': 'RadoRado', 'projection_id': 1,
         'row': 3, 'col': 5},
        {'username': 'RadoRado', 'projection_id': 1,
         'row': 7, 'col': 8},
        {'username': 'Ivo', 'projection_id': 3,
         'row': 1, 'col': 1},
        {'username': 'Ivo', 'projection_id': 3,
         'row': 1, 'col': 2},
        {'username': 'Mysterious', 'projection_id': 5,
         'row': 2, 'col': 3},
        {'username': 'Mysterious', 'projection_id': 5,
         'row': 2, 'col': 4},
    ]

    for movie in movies:
        cinema.add_movie(**movie)
    for projection in projections:
        cinema.add_projection(**projection)
    for reservation in reservations:
        cinema.add_reservation(**reservation)


def main():
    create_cinema_db()

if __name__ == '__main__':
    main()
