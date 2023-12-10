#!/usr/bin/python3
"""
   Module responsible for testing  BaseModel in base_model.py module
"""
import json
from datetime import datetime
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test class for BaseModel class"""

    def test_init(self):
        """Test BaseModel's constructor"""
        bm = BaseModel()
        self.assertTrue(isinstance(bm, BaseModel))

    def test_init_with_attributes(self):
        """Test BaseModel's constructor with attributes"""
        bm = BaseModel(id="123", created_at=datetime(2022, 1, 1),
                       updated_at=datetime(2022, 1, 2))
        self.assertEqual(bm.id, "123")
        self.assertEqual(bm.created_at, datetime(2022, 1, 1))
        self.assertEqual(bm.updated_at, datetime(2022, 1, 2))

    def test_str(self):
        """Testing __str__ method for BaseModel"""
        bm = BaseModel()
        expd_output = f"[BaseModel] ({bm.id}) {bm.__dict__}"
        self.assertEqual(str(bm), expd_output)

    def test_save(self):
        """Test save BaseModel method"""
        bm = BaseModel()
        prev_updated_at = bm.updated_at
        bm.save()
        new_updated_at = bm.updated_at
        self.assertNotEqual(prev_updated_at, new_updated_at)

    def test_to_dict(self):
        """Testing to_dict method in BaseModel class"""
        bm = BaseModel()
        expected_dict = {
            'id': bm.id,
            'created_at': bm.created_at.isoformat(),
            'updated_at': bm.updated_at.isoformat(),
            '__class__': bm.__class__.__name__
        }
        self.assertEqual(bm.to_dict(), expected_dict)

    def test_to_dict_method_custom_attributes(self):
        """Test to_dict method with custom attribute values"""
        bm = BaseModel()
        bm.first_name = "John"
        bm.age = 89
        expected_dict = {
            'id': bm.id,
            'created_at': bm.created_at.isoformat(),
            'updated_at': bm.updated_at.isoformat(),
            '__class__': bm.__class__.__name__,
            'first_name': 'John',
            'age': 89
        }
        self.assertEqual(bm.to_dict(), expected_dict)

    # Test serialization and deserialization to python and back
    def test_attribute_manipulation(self):
        """ Test attribute manipulation of class BaseModel inst"""
        bm = BaseModel()
        bm.first_name = "Moh"
        bm.age = 89
        self.assertEqual(bm.first_name, "Moh")
        self.assertEqual(bm.age, 89)

    # Test to check existing atrributes
    def test_attr(self):
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))


if __name__ == "__main__":
    unittest.main()
