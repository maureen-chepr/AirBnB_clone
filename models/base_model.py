#!/usr/bin/python3
"""
    Class BaseModel which is the super class for all other classes
"""
import uuid
from datetime import datetime
from models.__init__ import storage

class BaseModel:
    """
       Class that defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """Initializes BaseModel instances"""
        if kwargs:
              for key, value in kwargs.items():
                if key is not "__class__":
                    setattr(self, key, value)
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        #to check if self should be **kwargs
        storage.new(self)

    def __str__(self):
        """String representation of class BaseModel"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        self.save(storage)

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance"""
        attrs = self.__dict__.copy()
        attrs['__class__'] = self.__class__.__name__
        attrs['created_at'] = self.created_at.isoformat()
        attrs['updated_at'] = self.updated_at.isoformat()
        return attrs


