from sqlalchemy import Column, Integer, String
from connections import *


class Player(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    highscore = Column(Integer, default=0)
