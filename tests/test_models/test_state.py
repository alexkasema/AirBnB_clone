#!/usr/bin/python3

"""Test for State Class """

import unittest
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    """ Class for testing State class attributes """

    def setUp(self):
        """ Instance of State class """
        self.state = State()

    def tearDown(self):
        """ Set the instance created to None """
        self.state = None

    def test_instance_type(self):
        """ Test the type the instance belongs to """
        self.assertEqual(type(self.state), State)
        self.assertEqual(isinstance(self.state, State), True)
        self.assertEqual(issubclass(self.state.__class__, State), True)

    def test_set_attribute(self):
        """ Test setting of an attribute """
        State.name = "California"

        self.assertEqual(State.name, "California")

    def test_name(self):
        """ Test the name class attribute """
        self.assertEqual(type(self.state.name), str)
        self.assertEqual(type(State.name), str)

    def test_str_method(self):
        """ Test the str return method of the State class """
        obj_str = str(self.state)
        key = "[State] ({})".format(self.state.id)

        test = key in obj_str
        self.assertEqual(test, True)

        test = "created_at" in obj_str
        self.assertEqual(test, True)

        test = "updated_at" in obj_str
        self.assertEqual(test, True)

    def test_to_dict_method(self):
        """ Test to_dict method inherited from BaseModel """
        my_dict = self.state.to_dict()

        self.assertEqual(my_dict['id'], self.state.id)

        self.assertEqual(my_dict['__class__'], self.state.__class__.__name__)

        self.assertEqual(type(my_dict['updated_at']), str)
        self.assertEqual(type(self.state.updated_at), datetime)
