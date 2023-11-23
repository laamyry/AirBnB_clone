#!/usr/bin/python3
'''state'''
import unittest
from models.state import State
from datetime import datetime as date


class StateTestCase(unittest.TestCase):

    def test_state(self):
        new = State()
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertTrue(hasattr(new, "name"))

        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, date)
        self.assertIsInstance(new.updated_at, date)
        self.assertIsInstance(new.name, str)


if __name__ == '__main__':
    unittest.main()
