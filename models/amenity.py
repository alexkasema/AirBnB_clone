#!/usr/bin/python3
"""
The First Amenity
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """An Amenity class that inherits from BaseModel.
    Attributes:
        name (str): public class attribute
    """
    name = ''

    def __init__(self, *args, **kwargs):
        """instantiating an instance of an amenity.
        Args:
            args (list): A list with arguments.
            kwargs: (dict): A dictionary with arguments
        """
        super().__init__(*args, **kwargs)
