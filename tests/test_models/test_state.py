#!/usr/bin/python3
"""Test cases for State subclass"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Class test for testing State class"""

    def test_subclass(self):
        """Test if State is a subclass of BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_att(self):
        """Test if State has the expected attributes"""
        state = State()
        self.assertTrue(hasattr(state, 'name'))

    def test_attr_value(self):
        """Test if State attributes have default values"""
        state = State()
        self.assertEqual(state.name, "")

    def test_attr_type(self):
        """Test if State attributes have the correct types"""
        state = State()
        self.assertIsInstance(state.name, str)

    def test_to_dict(self):
        """Test if to_dict method returns the expected dictionary"""
        state = State()
        state.name = "Nakuru"

        expected_dict = {
            'id': state.id,
            'created_at': state.created_at.isoformat(),
            'updated_at': state.updated_at.isoformat(),
            'name': "Nakuru",
            '__class__': 'State'
        }

        self.assertEqual(state.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
