#!/usr/bin/python3
"""
   Module responsible for testing  BaseModel in base_model.py module
"""
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
        self.assertEqual(bm.first_name, "Moh")
