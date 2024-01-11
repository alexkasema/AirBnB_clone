#!/usr/bin/python3
"""Test for FileStorage class"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """
    A class that runs tests on FileStorage class properties
    """
    
    test_file = ""

    def setUp(self):
        """setting up an instance of every test"""
        self.test_file = 'test_file.json'
        self.test_objs = [BaseModel(), BaseModel(), BaseModel()]

        for obj in self.test_objs:
            storage.new(obj)
        storage.save()

    def tearDown(self):
        """deleting the objects"""
        del self.test_objs

    def test_type_storage(self):
        """test the type of storage variable"""
        self.assertIsInstance(storage, FileStorage)
        self.assertEqual(type(storage), FileStorage)

    def test_new_method(self):
        """test the new method in FileStorage class"""
        obj = BaseModel()

        storage.new(obj)
        my_objs = storage.all()

        key = obj.__class__.__name__ + '.' + str(obj.id)

        self.assertEqual(my_objs[key] is obj, True)

    def test_save_method(self):
        """Test the save method of the FileStorage class"""
        with open('file.json', 'r', encoding='utf-8') as f:
            my_file = f.read()

        self.assertNotEqual(len(my_file), 0)

    def test_reload_method(self):
        """test the reload method of the FileStorage class"""
        storage.reload()
        my_objs = storage.all()

        key = self.test_objs[2].__class__.__name__ + '.'
        key += str(self.test_objs[2].id)

        self.assertNotEqual(my_objs[key], None)
        self.assertEqual(my_objs[key].id, self.test_objs[2].id)
