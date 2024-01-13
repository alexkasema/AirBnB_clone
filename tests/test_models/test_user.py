#!/usr/bin/python3

"""Test for User Class """

import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    """ Class for testing User class attributes """

    def setUp(self):
        """ Instance of User class """
        self.user = User()

    def tearDown(self):
        """ Set the instance created to None """
        self.user = None

    def test_instance_type(self):
        """ Test the type the instance belongs to """
        self.assertEqual(type(self.user), User)
        self.assertEqual(isinstance(self.user, User), True)
        self.assertEqual(issubclass(self.user.__class__, User), True)

    def test_set_attribute(self):
        """ Test setting of an attribute """
        self.user.first_name = "Alex"
        self.user.last_name = "Smith"
        self.user.email = "a@s.elf"

        self.assertEqual(self.user.first_name, "Alex")
        self.assertEqual(self.user.last_name, "Smith")
        self.assertEqual(self.user.email, "a@s.elf")

    def test_email(self):
        """ Test the email class attribute """
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(User.email), str)

    def test_first_name(self):
        """ Test the first_name attribute """
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(User.first_name), str)

    def test_last_name(self):
        """ Test the last_name attribute """
        self.assertEqual(type(self.user.last_name), str)
        self.assertEqual(type(User.last_name), str)

    def test_password(self):
        """ Test the password attribute """
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(User.password), str)

    def test_str_method(self):
        """ Test the str return method of the User class """
        obj_str = str(self.user)
        key = "[User] ({})".format(self.user.id)

        test = key in obj_str
        self.assertEqual(test, True)

        test = "created_at" in obj_str
        self.assertEqual(test, True)

        test = "updated_at" in obj_str
        self.assertEqual(test, True)

    def test_to_dict_method(self):
        """ Test to_dict method inherited from BaseModel """
        my_dict = self.user.to_dict()

        self.assertEqual(my_dict['id'], self.user.id)

        self.assertEqual(my_dict['__class__'], self.user.__class__.__name__)
        self.assertEqual(my_dict['created_at'],
                                 self.user.created_at.isoformat())

        self.assertEqual(type(my_dict['updated_at']), str)
        self.assertEqual(type(self.user.updated_at), datetime)
