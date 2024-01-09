#!/usr/bin/python3
"""Test for BaseModel Class"""

import unittest
import uuid

from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """A class for testing BaseModel class methods """

    def setUp(self):
        """Setup an instance of BaseModel"""
        self.TestModel = BaseModel()

    def tearDown(self):
        """Set the instance created None"""
        self.TestModel = None

    def test_type_instance(self):
        """Test the type of created instance"""
        self.assertEqual(type(self.TestModel), BaseModel)
        self.assertIsInstance(self.TestModel, BaseModel)

    def test_unique_id(self):
        """Test the id of instances created"""
        test1 = BaseModel()
        test2 = BaseModel()

        self.assertNotEqual(test1.id, test2.id)
        self.assertNotEqual(self.TestModel.id, test1.id)

    def test_id_is_str(self):
        """Test if id is a string"""
        self.assertEqual(type(self.TestModel.id), str)

    def test_save_method(self):
        """Test if time is updated"""
        time1 = self.TestModel.updated_at
        self.TestModel.save()
        time2 = self.TestModel.updated_at

        self.assertNotEqual(time1, time2)
        self.assertEqual(type(time1), datetime)

    def test_to_dict(self):
        """Test to_dict method"""
        my_dict = self.TestModel.to_dict()
        self.assertEqual(my_dict['created_at'],
                         self.TestModel.created_at.isoformat())
        self.assertEqual(my_dict['__class__'],
                         self.TestModel.__class__.__name__)
        self.assertEqual(type(my_dict['created_at']), str)
        self.assertEqual(my_dict['id'], self.TestModel.id)

