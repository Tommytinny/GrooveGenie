#!/usr/bin/python3

from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship

class UserSongInteraction(BaseModel, Base):
    """ UserSongInteraction Details
    Attributes:
        liked (int): song liked.
        playCount (int): Song playcount.
        lastPlayedDate (date): Song last played date.
    """
    __tablename__ = 'UserSongInteractions'

    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    song_id = Column(String(60), ForeignKey('songs.id'), nullable=False)

    liked = Column(Integer, nullable=True)
    playCount = Column(Integer, nullable=True)
    lastPlayedDate = Column(DateTime, nullable=True)

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
