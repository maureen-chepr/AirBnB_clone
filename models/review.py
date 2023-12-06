#!/usr/bin/python3
"""
    Review class that inherits BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This is class Review"""
    place_id = ""
    user_id = ""
    text = ""
