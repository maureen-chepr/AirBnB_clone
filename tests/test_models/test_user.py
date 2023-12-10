#!/usr/bin/python3
"""
Module for testing class User
"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Class test for testing User class"""

    def test_init(self):  # ask ken why this yet we dont have init in user
        """Test class User's constructor"""
        u = User()
        self.assertTrue(isinstance(u, User))

    def test_subclass(self):
        """Test if User is a subclass of BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_attr(self):
        """Test if User has the expected attributes"""
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_attributes_default_values(self):
        """Test if User attributes have default values"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_attr_types(self):
        """Test if User attributes have the correct types"""
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_to_dict(self):
        """Test if to_dict method returns the expected dictionary"""
        user = User()
        user.email = "ken@example.com"
        user.password = "password"
        user.first_name = "John"
        user.last_name = "ken"

        expected_dict = {
            'id': user.id,
            'created_at': user.created_at.isoformat(),
            'updated_at': user.updated_at.isoformat(),
            'email': "ken@example.com",
            'password': "password",
            'first_name': "John",
            'last_name': "ken",
            '__class__': 'User'
        }

        self.assertEqual(user.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
