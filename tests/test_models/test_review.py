#!/usr/bin/python3
'''Review'''
import unittest
from models.review import Review
from datetime import datetime as date


class ReviewTestCase(unittest.TestCase):

    def test_review(self):
        new = Review()
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertTrue(hasattr(new, "place_id"))
        self.assertTrue(hasattr(new, "user_id"))
        self.assertTrue(hasattr(new, "text"))

        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, date)
        self.assertIsInstance(new.updated_at, date)
        self.assertIsInstance(new.place_id, str)
        self.assertIsInstance(new.user_id, str)
        self.assertIsInstance(new.text, str)


if __name__ == '__main__':
    unittest.main()
