from sqlalchemy import desc
from sqlalchemy import delete

from movie import Movie
from projection import Projection
from reservation import Reservation
from connections import *


class Cinema:

    def __init__(self, rows, cols):
        Base.metadata.create_all(engine)
        self.__session = Session()
        self.__rows = rows
        self.__cols = cols

    def get_rows(self):
        return self.__rows

    def get_cols(self):
        return self.__cols

    def add_movie(self, name, rating):
        self.__session.add(Movie(name=name, rating=rating))
        self.__session.commit()

    def add_projection(self, movie_id, type, date, time):
        self.__session.add(Projection(
            movie_id=movie_id, type=type, date=date, time=time))
        self.__session.commit()

    def add_reservation(self, username, projection_id, row, col):
        self.__session.add(
            Reservation(
                username=username, projection_id=projection_id,
                row=row, col=col))
        self.__session.commit()

    def show_movies(self):
        all_movies = self.__session.query(
            Movie).order_by(desc(Movie.rating)).all()
        movies_strings = [str(movie) for movie in all_movies]
        return '\n'.join(movies_strings)

    def show_movie_projections(self, movie_id, date=None):
        if date:
            projections = self.__session.query(Projection).filter(
                movie_id == Projection.movie_id,
                date == Projection.date).order_by(
                date).order_by(Projection.time).all()
            projections_strings = [
                projection.str_without_date() for projection in projections]
        else:
            projections = self.__session.query(Projection).filter(
                movie_id == Projection.movie_id).order_by(
                date).order_by(Projection.time).all()
            projections_strings = [str(projection)
                                   for projection in projections]
        return {'movie_name': projections[0].movie.name,
                'projections_details': '\n'.join(projections_strings)}

    def get_occupied_seats(self, projection_id):
        projection = self.__session.query(Projection).filter(
            projection_id == Projection.id).one()
        return projection.get_occupied_seats()

    def get_reservation(self, movie_id, projection_id):
        projection = self.__session.query(Projection).filter(
            projection_id == Projection.id,
            movie_id == Projection.movie_id).one()
        reservation_info = {
            'movie_name': projection.movie.name,
            'rating': projection.movie.rating,
            'date': projection.date,
            'time': projection.time,
            'type': projection.type,
            'seats': [(r.row, r.col) for r in projection.reservations]
        }
        return reservation_info

    def cancel_reservation(self, name):
        self.__session.query(Reservation).filter(
            name == Reservation.username).delete()
        self.__session.commit()
