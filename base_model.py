#!/usr/bin/python3
'''Module for the BaseModel class.'''
import uuid
from datetime import datetime as date


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = date.now()
        self.updated_at = date.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        self.updated_at = date.now()

    def to_dict(self):
        model_dict = self.__dict__.copy()
        model_dict['__class__'] = self.__class__.__name__
        model_dict['created_at'] = self.created_at.isoformat()
        model_dict['updated_at'] = self.updated_at.isoformat()
        return model_dict
