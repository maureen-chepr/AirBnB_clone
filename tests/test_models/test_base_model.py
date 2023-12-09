#!/usr/bin/python3
"""
   Module responsible for testing  BaseModel in base_model.py module
"""
from datetime import datetime
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test class for BaseModel class"""

    #def SetUpClass(cls):
        #"""Does setup operatons before every test method"""
        #cls.bm_inst = Basemodel()

    #def tearDownClass(cls):
        #"""Does clean up operations for every test case"""
        #del cls.bm_inst

    def test_init(self):
        """Test BaseModel's constructor"""
        bm = BaseModel()
        self.assertTrue(isinstance(bm, BaseModel))

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
    #def test_save(self):
        #"""Test save BaseModel method"""


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
        bm.age = 89 # shit I need to show this to Moh, sijui vile inapass
        expected_dict = {
            'id': bm.id,
            'created_at': bm.created_at.isoformat(),
            'updated_at': bm.updated_at.isoformat(),
            '__class__': bm.__class__.__name__,
            'first_name': 'John',
            'age': 89
        }
        self.assertEqual(bm.to_dict(), expected_dict)

    #Test serialization and deserialization to python and back
    def test_attribute_manipulation(self):
        """ Test attribute manipulation of class BaseModel inst"""
        bm = BaseModel()
        bm.first_name = "Moh"
        bm.age = 89
        self.assertEqual(bm.first_name, "Moh")
        self.assertEqual(bm.age, 89)

    #test __init__
    def test_init_with_keyword_arguments(self):
        """Test initializing BaseModel with specific attributes using keyword arguments."""
        ken_id = "ken_id"
        ken_created_at = datetime(2023, 1, 1)
        ken_updated_at = datetime(2023, 1, 2)

    # Initialize BaseModel with custom attributes using keyword arguments
        bm = BaseModel(
            id=ken_id,
            created_at=ken_created_at,
            updated_at=ken_updated_at,
            ken_attr="tester"
        )

    # Check if the instance is initialized with the correct values
        self.assertEqual(bm.id, ken_id)
        self.assertEqual(bm.created_at, ken_created_at)
        self.assertEqual(bm.updated_at, ken_updated_at)

    # Ensure that the custom attribute is set
        self.assertEqual(getattr(bm, "ken_attr", None), "tester")

    # Check if the instance is stored in the storage
        self.assertIn(ken_id, storage.all())
