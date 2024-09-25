#!/usr/bin/python3

from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey

class Playlist(BaseModel, Base):
    """ Playlist Details
    Attributes:
        name (str): Playlist name.
    """
    __tablename__ = 'playlists'

    name = Column(String(128), nullable=False)

    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    song_id = Column(String(60), ForeignKey('songs.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
