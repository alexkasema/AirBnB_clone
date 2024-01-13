#!/usr/bin/python3

""" The State module """

from base.base_model import BaseModel


class State(BaseModel):
    """ A state class that inherits from BaseModel.
    Attributes:
        name (string): public class attribute.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Instantiating an instance of a User.
        Args:
            args (list): A list with arguments.
            kwargs (dict): A dictionary of arguments.
        """
        super().__init__(*args, **kwargs)
