#!/usr/bin/python3
""" unit test for bases """
import json
import unittest
from models.base_model import BaseModel as base
from datetime import datetime as date
import models
from io import StringIO
import sys
from unittest.mock import patch
captured_output = StringIO()
sys.stdout = captured_output


class BaseModelTestCase(unittest.TestCase):

    def setUp(self):
        self.filepath = models.storage._FileStorage__file_path
        with open(self.filepath, 'w') as file:
            file.truncate(0)
        models.storage.all().clear()

    def tearDown(self):
        printed_output = captured_output.getvalue()
        sys.stdout = sys.__stdout__

    def test_basemodel_init(self):
        new = base()

        self.assertTrue(hasattr(new, "__init__"))
        self.assertTrue(hasattr(new, "__str__"))
        self.assertTrue(hasattr(new, "save"))
        self.assertTrue(hasattr(new, "to_dict"))

        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))

        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, date)
        self.assertIsInstance(new.updated_at, date)

        keyname = "BaseModel."+new.id
        self.assertIn(keyname, models.storage.all())
        self.assertTrue(models.storage.all()[keyname] is new)

        new.name = "My First Model"
        new.my_number = 89
        self.assertTrue(hasattr(new, "name"))
        self.assertTrue(hasattr(new, "my_number"))
        self.assertTrue(hasattr(models.storage.all()[keyname], "name"))
        self.assertTrue(hasattr(models.storage.all()[keyname], "my_number"))

        old_time = new.updated_at
        new.save()
        self.assertNotEqual(old_time, new.updated_at)
        self.assertGreater(new.updated_at, old_time)

        with patch('models.storage.save') as mock_function:
            obj = base()
            obj.save()
            mock_function.assert_called_once()

        keyname = "BaseModel."+new.id
        with open(self.filepath, 'r') as file:
            saved_data = json.load(file)
        self.assertIn(keyname, saved_data)
        self.assertEqual(saved_data[keyname], new.to_dict())

    def test_basemodel_init2(self):

        new = base()
        new.name = "John"
        new.my_number = 89
        new2 = base(**new.to_dict())
        self.assertEqual(new.id, new2.id)
        self.assertEqual(new.name, "John")
        self.assertEqual(new.my_number, 89)
        self.assertEqual(new.to_dict(), new2.to_dict())

    def test_basemodel_init3(self):
        new = base()
        new2 = base(new.to_dict())
        self.assertNotEqual(new, new2)
        self.assertNotEqual(new.id, new2.id)
        self.assertTrue(isinstance(new2.created_at, date))
        self.assertTrue(isinstance(new2.updated_at, date))

        new = base()

        self.assertEqual(
            str(new),  f"[BaseModel] ({new.id}) {new.__dict__}")

        old_time = new.updated_at
        new.save()
        self.assertGreater(new.updated_at, old_time)


if __name__ == '__main__':
    unittest.main()
