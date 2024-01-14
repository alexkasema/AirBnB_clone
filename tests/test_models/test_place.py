#!/usr/bin/python3

"""Test for Place Class """

import unittest
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):
    """ Class for testing User class attributes """

    def setUp(self):
        """ Instance of Place class """
        self.place = Place()

    def tearDown(self):
        """ Set the instance created to None """
        self.place = None

    def test_instance_type(self):
        """ Test the type the instance belongs to """
        self.assertEqual(type(self.place), Place)
        self.assertEqual(isinstance(self.place, Place), True)
        self.assertEqual(issubclass(self.place.__class__, Place), True)

    def test_set_attribute(self):
        """ Test setting of an attribute """
        self.place.description = "Beautiful Rivers"
        self.place.max_guest = 4

        self.assertEqual(self.place.description, "Beautiful Rivers")

    def test_city_id(self):
        """ Test the city_id class attribute """
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(Place.city_id), str)

    def test_user_id(self):
        """ Test the user_id attribute """
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(Place.user_id), str)

    def test_name(self):
        """ Test the name attribute """
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(Place.name), str)

    def test_description(self):
        """ Test the description attribute """
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(Place.description), str)

    def test_number_rooms(self):
        """ Test the number_rooms attribute """
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(Place.number_rooms), int)

    def test_number_bathrooms(self):
        """ Test the number_bathrooms attribute """
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(Place.number_bathrooms), int)

    def test_max_guest(self):
        """ Test the max_guest attribute """
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(Place.max_guest), int)

    def test_price_by_night(self):
        """ Test the price_by_night attribute """
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(Place.price_by_night), int)

    def test_latitude(self):
        """ Test the latitude attribute """
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(Place.latitude), float)

    def test_longitude(self):
        """ Test the longitude attribute """
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(Place.longitude), float)

    def test_str_method(self):
        """ Test the str return method of the User class """
        obj_str = str(self.place)
        key = "[Place] ({})".format(self.place.id)

        test = key in obj_str
        self.assertEqual(test, True)

        test = "created_at" in obj_str
        self.assertEqual(test, True)

        test = "updated_at" in obj_str
        self.assertEqual(test, True)

    def test_to_dict_method(self):
        """ Test to_dict method inherited from BaseModel """
        my_dict = self.place.to_dict()

        self.assertEqual(my_dict['id'], self.place.id)

        self.assertEqual(my_dict['__class__'], self.place.__class__.__name__)

        self.assertEqual(type(my_dict['updated_at']), str)
        self.assertEqual(type(self.place.updated_at), datetime)

    def test_from_dict(self):
        """ Test creating instances from dictionary """
        my_dict = self.place.to_dict()
        test1 = Place(**my_dict)

        self.assertEqual(test1.id, self.place.id)
        self.assertEqual(test1.created_at, self.place.created_at)
        self.assertEqual(test1.updated_at, self.place.updated_at)
        self.assertEqual(test1.__class__.__name__,
                         self.place.__class__.__name__)
