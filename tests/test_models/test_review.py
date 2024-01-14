#!/usr/bin/python3

"""Test for Review Class """

import unittest
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    """ Class for testing Review class attributes """

    def setUp(self):
        """ Instance of Review class """
        self.review = Review()

    def tearDown(self):
        """ Set the instance created to None """
        self.review = None

    def test_instance_type(self):
        """ Test the type the instance belongs to """
        self.assertEqual(type(self.review), Review)
        self.assertEqual(isinstance(self.review, Review), True)
        self.assertEqual(issubclass(self.review.__class__, Review), True)

    def test_set_attribute(self):
        """ Test setting of an attribute """
        Review.place_id = "t-24"
        Review.user_id = "r-67"
        Review.text = "good service"

        self.assertEqual(Review.place_id, "t-24")
        self.assertEqual(Review.user_id, "r-67")
        self.assertEqual(Review.text, "good service")

    def test_place_id(self):
        """ Test the place_id class attribute """
        self.assertEqual(type(self.review.place_id), str)
        self.assertEqual(type(Review.place_id), str)

    def test_user_id(self):
        """ Test the user_id class attribute """
        self.assertEqual(type(self.review.user_id), str)
        self.assertEqual(type(Review.user_id), str)

    def test_text(self):
        """ Test the text class attribute """
        self.assertEqual(type(self.review.text), str)
        self.assertEqual(type(Review.text), str)

    def test_str_method(self):
        """ Test the str return method of the Review class """
        obj_str = str(self.review)
        key = "[Review] ({})".format(self.review.id)

        test = key in obj_str
        self.assertEqual(test, True)

        test = "created_at" in obj_str
        self.assertEqual(test, True)

        test = "updated_at" in obj_str
        self.assertEqual(test, True)

    def test_to_dict_method(self):
        """ Test to_dict method inherited from BaseModel """
        my_dict = self.review.to_dict()

        self.assertEqual(my_dict['id'], self.review.id)

        self.assertEqual(my_dict['__class__'], self.review.__class__.__name__)

        self.assertEqual(type(my_dict['updated_at']), str)
        self.assertEqual(type(self.review.updated_at), datetime)
