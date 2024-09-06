#!/usr/bin/python3
"""
initialize the models package
"""
from os import getenv

storage_type = "db"

if storage_type == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
