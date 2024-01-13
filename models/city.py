#!/usr/bin/python3

""" The City module """

from base.base_model import BaseModel


class City(BaseModel):
    """ A City class that inherits from BaseModel.
    Attributes:
        state_id (str): it will be the State.id
        name (str): public class attribute.
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ Instantiating an instance of a City.
        Args:
            args (list): A list with arguments.
            kwargs (dict): A dictionary of arguments.
        """
        super().__init__(*args, **kwargs)
