#!/usr/bin/python3

"""Test for City Class """

import unittest
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    """ Class for testing City class attributes """

    def setUp(self):
        """ Instance of City class """
        self.city = City()

    def tearDown(self):
        """ Set the instance created to None """
        self.city = None

    def test_instance_type(self):
        """ Test the type the instance belongs to """
        self.assertEqual(type(self.city), City)
        self.assertEqual(isinstance(self.city, City), True)
        self.assertEqual(issubclass(self.city.__class__, City), True)

    def test_set_attribute(self):
        """ Test setting of an attribute """
        City.state_id = "a-24"
        City.name = "Mombasa"

        self.assertEqual(City.state_id, "a-24")
        self.assertEqual(City.name, "Mombasa")

    def test_state_id(self):
        """ Test the state_id class attribute """
        self.assertEqual(type(self.city.state_id), str)
        self.assertEqual(type(City.state_id), str)

    def test_name(self):
        """ Test the name class attribute """
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(City.name), str)

    def test_str_method(self):
        """ Test the str return method of the City class """
        obj_str = str(self.city)
        key = "[City] ({})".format(self.city.id)

        test = key in obj_str
        self.assertEqual(test, True)

        test = "created_at" in obj_str
        self.assertEqual(test, True)

        test = "updated_at" in obj_str
        self.assertEqual(test, True)

    def test_to_dict_method(self):
        """ Test to_dict method inherited from BaseModel """
        my_dict = self.city.to_dict()

        self.assertEqual(my_dict['id'], self.city.id)

        self.assertEqual(my_dict['__class__'], self.city.__class__.__name__)

        self.assertEqual(type(my_dict['updated_at']), str)
        self.assertEqual(type(self.city.updated_at), datetime)
