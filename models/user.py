#!/usr/bin/python3
"""
    User class that inherits BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """This is the User class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
