#!/usr/bin/python3
"""
Module for testing class User
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Class test for testing User class"""

    def test_init(self):
        """Test class User's constructor"""
        u = User()
        self.assertTrue(isinstance(u, User)) 
