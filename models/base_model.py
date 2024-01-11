#!/usr/bin/python3

""" The Base Model """
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """ Instantiating instance of BaseModel class """

        if len(kwargs) > 0:
            for k, v in kwargs.items():
                if k in ['created_at', 'updated_at']:
                    self.__dict__[k] = datetime\
                                       .strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                elif k == 'id':
                    self.id = v
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Returns the informal string representation of object instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
         updates the public instance attribute updated_at with
         the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
