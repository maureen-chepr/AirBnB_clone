#!/usr/bin/python3
"""
Class FileStorage saves json to files for persistence
"""
import json


class FilesStoage:
    """
    serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = #"file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """ serializes instances to a JSON file and deserializes JSON file
            to instances
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__object[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        serl_objs = {}
        for key, obj in self.__objects.items():
            serl_objs[key] = obj.to_dict()

        with open(self.__file__path, 'w') as file:
            json.dump(serl_objs, file)
