#!/usr/bin/python3

from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """ User Details
    Attributes:
        username (str): User first name.
        password (str): User password.
        email (str): User email.
    """
    
    __tablename__ = 'users'

    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(60), unique=True, nullable=False)
    email = Column(String(120), nullable=False)

    liked_songs = relationship("UserSongInteraction", backref="user")
    
    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
