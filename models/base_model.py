#!/usr/bin/python3
"""
BaseModel Class
"""

from datetime import datetime
import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class BaseModel:
    """The BaseModel Class"""
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            self.id = str(uuid.uuid4())
                #print("{}: {}".format(key, value))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """updates 'update_at' with the current datetime"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """return dictionary of the instance"""
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__._name__
        return inst_dict

    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)
