#!/usr/bin/python3

from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship

class Song(BaseModel, Base):
    """ Song Details
    Attributes:
        title (str): Song title.
        artist (str): Song artist.
        album (str): Song album.
        genre (str): Song genre.
        releaseYear (str): Song release year.
    """
    __tablename__ = 'songs'

    title = Column(String(200), nullable=False)
    artist = Column(String(200), nullable=False)
    genre = Column(String(100), nullable=False)
    tempo = Column(Float)
    popularity = Column(Integer)

    liked_by_user = relationship("UserSongInteraction", backref="song")

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
