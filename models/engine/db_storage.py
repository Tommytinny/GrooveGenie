#!/usr/bin/python3
"""
Database Storage class
"""
import models
from models.base_model import Base
from models.user import User
from models.play_list import Playlist
from models.song import Song
from models.user_song_interact import UserSongInteraction
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"User": User, "Playlist": Playlist, "Song": Song,
           "UserSongInteraction": UserSongInteraction}

class DBStorage:
    """Database class"""
    __engine = None
    __session = None

    def __init__(self):
        mysql_user = "admin"
        mysql_pwd = "Wakeup_11!"
        mysql_host = "localhost"
        mysql_db = "groovie_db"
        self.__engine = create_engine('mysql+pymysql://{}:{}@{}/{}'.
                                      format(mysql_user,
                                             mysql_pwd,
                                             mysql_host,
                                             mysql_db))
    
    def all(self, cls=None):
        """query on all current session"""
        new_dict = {}
        """if cls is None:
            for clss in classes:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj"""
        if cls is not None:
            for clss in classes:
                if cls is None or cls is classes[clss] or cls is clss:
                    objs = self.__session.query(classes[clss]).all()
                    for obj in objs:
                        if hasattr(obj, '_sa_instance_state'):
                            delattr(obj, '_sa_instance_state')
                        key = obj.__class__.__name__ + '.' + obj.id
                        new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(Self, obj=None):
        """delete from the current database session if obj is not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        session_fact = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_fact)
        self.__session = Session
