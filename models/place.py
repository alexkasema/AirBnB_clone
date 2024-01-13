#!/usr/bin/python3

""" The Place module """

from base.base_model import BaseModel


class Place(BaseModel):
    """ A Place class that inherits from BaseModel.
    Attributes:
        name (str): public class attribute.
        city_id (str): public class attribute, it will be the City.id
        user_id (str): public class attribute, it will be the User.id
        description (str): public class attribute.
        number_rooms (int): public class attribute.
        number_bathrooms (int): public class attribute.
        max_guest (int): public class attribute.
        price_by_night (int): public class attribute.
        latitude (float): public class attribute.
        longitude (float): public class attribute.
        amenity_ids (list): public class attribute.
                            it will be the list of Amenity.id later

    """
    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """ Instantiating an instance of a User.
        Args:
            args (list): A list with arguments.
            kwargs (dict): A dictionary of arguments.
        """
        super().__init__(*args, **kwargs)
