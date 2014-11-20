from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


from connections import *


class Projection(Base):
    HALL_SIZE = 100
    __tablename__ = "projections"
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey("movies.id"))
    movie = relationship('Movie', backref='projections')
    type = Column(String)
    date = Column(String)
    time = Column(String)

    def __str__(self):
        return '[{}] - {} {} ({}) - {} spots available'.format(
            self.id, self.date, self.time, self.type, self.calc_free_seats())

    def str_without_date(self):
        return '[{}] - {} ({})'.format(self.id, self.time, self.type)

    def get_occupied_seats(self):
        occupied_seats = [(r.row, r.col) for r in self.reservations]
        return occupied_seats

    def calc_free_seats(self):
        occupied_seats_number = len(self.get_occupied_seats())
        free_seat_number = Projection.HALL_SIZE - occupied_seats_number
        if free_seat_number < 0:
            return 0
        else:
            return free_seat_number
