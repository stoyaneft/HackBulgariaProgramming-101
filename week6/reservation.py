from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from connections import *


class Reservation(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    projection_id = Column(Integer, ForeignKey('projections.id'))
    projection = relationship('Projection', backref='reservations')
    row = Column(Integer)
    col = Column(Integer)
