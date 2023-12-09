#!/usr/bin/python3
"""
Class BaseModel which is the super class for all other classes
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
       Class that defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """Initializes BaseModel instances"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()#
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()#
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)  # Call new method on storage for new instances
        #self.first_name = ""

    def __str__(self):
        """String representation of class BaseModel"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at with the current datetime
        and calls the save method on storage"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance"""
        attrs = self.__dict__.copy()
        attrs['__class__'] = self.__class__.__name__
        # attrs['created_at'] = self.created_at.isoformat()
        # attrs['updated_at'] = self.updated_at.isoformat()
        if isinstance(attrs['created_at'], datetime):
            attrs['created_at'] = attrs['created_at'].isoformat()
        if isinstance(attrs['updated_at'], datetime):
            attrs['updated_at'] = attrs['updated_at'].isoformat()
        return attrs
