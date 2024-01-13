#!/usr/bin/python3
"""Store first object"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
                key_split = k.split('.')
                if key_split[0] == 'BaseModel':
                    FileStorage.__objects[k] = BaseModel(**v)
                elif key_split[0] == 'User':
                    FileStorage.__objects[k] = User(**v)
                elif key_split[0] == 'State':
                    FileStorage.__objects[k] = State(**v)
                elif key_split[0] == 'City':
                    FileStorage.__objects[k] = City(**v)
                elif key_split[0] == 'Amenity':
                    FileStorage.__objects[k] = Amenity(**v)
                elif key_split[0] == 'Place':
                    FileStorage.__objects[k] = Place(**v)
                elif key_split[0] == 'Review':
                    FileStorage.__objects[k] = Review(**v)
        except Exception:
            pass
