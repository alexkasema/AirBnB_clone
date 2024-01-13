#!/usr/bin/python3
"""
The Review Module
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """A Review class that inherits from BaseModel
    Attributes:
        place_id (str): public class attribute, it will be the Place.id
        user_id (str): public class attribute, it will be the User.id
        text (str): public class attribute, empty string
    """

    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        """instantiating an instance of a review
        Args:
            args (list): A list with arguments.
            kwargs: (dict): A dictionary with arguments
        """
        super().__init__(*args, **kwargs)
