#!/usr/bin/python3
"""
    User class that inherits BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """This is the User class"""
    def __init__(self, *args, **kwargs):
        """initializes the user class instances"""
        super().__init__(*args, **kwargs)
        
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
