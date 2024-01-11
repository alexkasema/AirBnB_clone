#!/usr/bin/python3
"""Store first object"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    serializes instances to a JSON file and deserializes JSON
    file to instances
    """
    __file_path = "file.json"
    __objects = dict()

    def __init__(self):
        """ Initialize instance of FileStorage class """
        pass

    def all(self):
        """  returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        dictionary = obj.to_dict()

        key = "{}.{}".format(dictionary['__class__'], str(obj.id))

        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        """

        dictionary = dict()
        for k, v in FileStorage.__objects.items():
            dictionary[k] = v.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(dictionary, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists.
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """

        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                my_dict = json.load(f)
            for k, v in my_dict.items():
                FileStorage.__objects[k] = BaseModel(**v)
        except Exception:
            pass
