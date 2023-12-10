#!/usr/bin/python3
"""Tests cases for Amenity subclass"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Class test for testing Amenity class"""

    def test_subclass(self):
        """Test if Amenity is a subclass of BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attr(self):
        """Test if Amenity has the expected attributes"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))

    def test_attr_values(self):
        """Test if Amenity attributes have default values"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_attr_type(self):
        """Test if Amenity attributes have the correct types"""
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)

    def test_to_dict(self):
        """Test if to_dict method returns the expected dictionary"""
        amenity = Amenity()
        amenity.name = "abc"

        expected_dict = {
            'id': amenity.id,
            'created_at': amenity.created_at.isoformat(),
            'updated_at': amenity.updated_at.isoformat(),
            'name': "abc",
            '__class__': 'Amenity'
        }

        self.assertEqual(amenity.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
