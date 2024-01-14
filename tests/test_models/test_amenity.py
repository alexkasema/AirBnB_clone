#!/usr/bin/python3

"""Test for Amenity Class """

import unittest
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """ Class for testing Amenity class attributes """

    def setUp(self):
        """ Instance of Amenity class """
        self.amenity = Amenity()

    def tearDown(self):
        """ Set the instance created to None """
        self.amenity = None

    def test_instance_type(self):
        """ Test the type the instance belongs to """
        self.assertEqual(type(self.amenity), Amenity)
        self.assertEqual(isinstance(self.amenity, Amenity), True)
        self.assertEqual(issubclass(self.amenity.__class__, Amenity), True)

    def test_set_attribute(self):
        """ Test setting of an attribute """
        Amenity.name = "Hotel"
        self.assertEqual(Amenity.name, "Hotel")

    def test_name(self):
        """ Test the name class attribute """
        self.assertEqual(type(self.amenity.name), str)
        self.assertEqual(type(Amenity.name), str)

    def test_str_method(self):
        """ Test the str return method of the Amenity class """
        obj_str = str(self.amenity)
        key = "[Amenity] ({})".format(self.amenity.id)

        test = key in obj_str
        self.assertEqual(test, True)

        test = "created_at" in obj_str
        self.assertEqual(test, True)

        test = "updated_at" in obj_str
        self.assertEqual(test, True)

    def test_to_dict_method(self):
        """ Test to_dict method inherited from BaseModel """
        my_dict = self.amenity.to_dict()

        self.assertEqual(my_dict['id'], self.amenity.id)

        self.assertEqual(my_dict['__class__'], self.amenity.__class__.__name__)

        self.assertEqual(type(my_dict['updated_at']), str)
        self.assertEqual(type(self.amenity.updated_at), datetime)
