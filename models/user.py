#!/usr/bin/python3
'''user file'''
from models.base_model import BaseModel as base


class User(base):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
