#!/usr/bin/python3
""" Test cases for subclass city"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Class test for testing City class"""

    def test_subclass(self):
        """Test if City is a subclass of BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_attrs(self):
        """Test if City has the expected attributes"""
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

    def test_attrs_values(self):
        """Test if City attributes have default values"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_attrs_types(self):
        """Test if City attributes have the correct types"""
        city = City()
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)

    def test_to_dict(self):
        """Test if to_dict method returns the expected dictionary"""
        city = City()
        city.state_id = "Nairobi"
        city.name = "Nai"

        expected_dict = {
            'id': city.id,
            'created_at': city.created_at.isoformat(),
            'updated_at': city.updated_at.isoformat(),
            'state_id': "Nairobi",
            'name': "Nai",
            '__class__': 'City'
        }

        self.assertEqual(city.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
