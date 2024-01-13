#!/usr/bin/python3
"""
The First User
"""

from models.base_model import BaseModel


class User(BaseModel):
    """A User class that inherits from BaseModel
    Attributes:
        email (str): public class attribute
        password (str): public class attribute
        first_name (str): public class attribute
        last-name (str): public class attribute
    """

    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """instantiating an instance of a user.
        Args:
            args (list): A list with arguments.
            kwargs: (dict): A dictionary with arguments
        """
        super().__init__(*args, **kwargs)
