#!/usr/bin/python3
"""Test cases for Place subclass"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Class test for testing Place class"""

    def test_subclass(self):
        """Test if Place is a subclass of BaseModel"""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_attres(self):
        """Test if Place has the expected attributes"""
        place = Place()
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(hasattr(place, 'description'))
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertTrue(hasattr(place, 'amenity_ids'))

    def test_attr_values(self):
        """Test if Place attributes have default values"""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, "")

    def test_attrs_types(self):
        """Test if Place attributes have the correct types"""
        place = Place()
        self.assertIsInstance(place.city_id, str)
        self.assertIsInstance(place.user_id, str)
        self.assertIsInstance(place.name, str)
        self.assertIsInstance(place.description, str)
        self.assertIsInstance(place.number_rooms, int)
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertIsInstance(place.max_guest, int)
        self.assertIsInstance(place.price_by_night, int)
        self.assertIsInstance(place.latitude, float)
        self.assertIsInstance(place.longitude, float)
        self.assertIsInstance(place.amenity_ids, str)

    def test_to_dict(self):
        """Test if to_dict method returns the expected dictionary"""
        place = Place()
        place.city_id = "123"
        place.user_id = "456"
        place.name = "Kempinski"
        place.description = "Beautiful wonders"
        place.number_rooms = 5
        place.number_bathrooms = 3
        place.max_guest = 3
        place.price_by_night = 50000
        place.latitude = 37.7749
        place.longitude = -122.4194
        place.amenity_ids = "123"

        expected_dict = {
            'id': place.id,
            'created_at': place.created_at.isoformat(),
            'updated_at': place.updated_at.isoformat(),
            'city_id': "123",
            'user_id': "456",
            'name': "Kempinski",
            'description': "Beautiful wonders",
            'number_rooms': 5,
            'number_bathrooms': 3,
            'max_guest': 3,
            'price_by_night': 50000,
            'latitude': 37.7749,
            'longitude': -122.4194,
            'amenity_ids': "123",
            '__class__': 'Place'
        }

        self.assertEqual(place.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
