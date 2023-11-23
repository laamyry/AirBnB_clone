#!/usr/bin/python3
'''Module for the BaseModel class.'''
from uuid import uuid4 as ud4
from datetime import datetime as date
import models


class BaseModel:
    def __init__(self, *args, **kwargs) -> None:
        self.id = str(ud4())
        self.created_at = date.now()
        self.updated_at = date.now()
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = date.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key != "__class__":
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self) -> str:
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self) -> None:
        self.updated_at = date.now()
        models.storage.save()

    def to_dict(self) -> dict:
        to_diction = dict(self.__dict__)
        to_diction["__class__"] = self.__class__.__name__
        if not isinstance(to_diction["created_at"], str):
            to_diction["created_at"] = to_diction["created_at"].isoformat()
        if not isinstance(to_diction["updated_at"], str):
            to_diction["updated_at"] = to_diction["updated_at"].isoformat()
        return to_diction
