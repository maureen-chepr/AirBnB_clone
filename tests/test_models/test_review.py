#!/usr/bin/python3
"""Test cases for Review subclass"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Class test for testing Review class"""

    def test_subclass(self):
        """Test if Review is a subclass of BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attrs(self):
        """Test if Review has the expected attributes"""
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))

    def test_attrs_values(self):
        """Test if Review attributes have default values"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_attrs_types(self):
        """Test if Review attributes have the correct types"""
        review = Review()
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)

    def test_to_dict(self):
        """Test if to_dict method returns the expected dictionary"""
        review = Review()
        review.place_id = "143"
        review.user_id = "459"
        review.text = "Great experience"

        expected_dict = {
            'id': review.id,
            'created_at': review.created_at.isoformat(),
            'updated_at': review.updated_at.isoformat(),
            'place_id': "143",
            'user_id': "459",
            'text': "Great experience",
            '__class__': 'Review'
        }

        self.assertEqual(review.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
