#!/usr/bin/python3
"""Test cases for file storage"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.state import State


class TestFileStorage(unittest.TestCase):
    """Class test for testing FileStorage class"""

    def test_all(self):
        """Test the all method"""
        file_storage = FileStorage()
        state = State()
        file_storage.new(state)
        all_objects = file_storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertIn("State.{}".format(state.id), all_objects)

    def test_new(self):
        """Test the new method"""
        file_storage = FileStorage()
        state = State()
        file_storage.new(state)
        all_objects = file_storage.all()
        self.assertIn("State.{}".format(state.id), all_objects)

    def test_save_reload(self):
        """Test the save and reload methods"""
        file_path = "test_file.json"
        file_storage = FileStorage()
        file_storage._FileStorage__file_path = file_path
        state = State()
        file_storage.new(state)
        file_storage.save()

        # Check if the file was created
        self.assertTrue(os.path.isfile(file_path))

        new_file_storage = FileStorage()
        new_file_storage._FileStorage__file_path = file_path
        new_file_storage.reload()

        all_objects = new_file_storage.all()
        self.assertIn("State.{}".format(state.id), all_objects)

        # Clean up
        os.remove(file_path)


if __name__ == "__main__":
    unittest.main()
