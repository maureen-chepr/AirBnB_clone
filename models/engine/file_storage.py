#!/usr/bin/python3
"""
Class FileStorage saves json to files for persistence
"""
import json
from os.path import isfile


class FileStorage:
    """
    serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
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
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        serl_objs = {}
        for key, obj in self.__objects.items():
            serl_objs[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serl_objs, file)

    def reload(self):
        """deserializes the JSON file to __objects if filepath exists"""
        #filename = "{}.json".format(self.__class__.__name__)
        from models.base_model import BaseModel
        if isfile(self.__file_path):
            with open(self.__file_path, 'r') as file:
                json_str = file.read()
                if json_str:
                    dicto = json.loads(json_str)
                    class_mapping = {
                        'BaseModel': BaseModel,
                    }

                    for key, obj_data in dicto.items():
                        cls_name, obj_id = key.split('.')
                        class_type = class_mapping.get(cls_name)

                        if class_type:
                            obj_instance = class_type(**obj_data)
                            self.__objects[key] = obj_instance

                    return self.__objects
