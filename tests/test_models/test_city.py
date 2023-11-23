#!/usr/bin/python3
'''city'''
import unittest
from models.city import City
from datetime import datetime as date


class CityTestCase(unittest.TestCase):

    def test_city(self):
        new = City()
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertTrue(hasattr(new, "state_id"))
        self.assertTrue(hasattr(new, "name"))

        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, date)
        self.assertIsInstance(new.updated_at, date)
        self.assertIsInstance(new.state_id, str)
        self.assertIsInstance(new.name, str)


if __name__ == '__main__':
    unittest.main()
