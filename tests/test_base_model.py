#!/usr/bin/python3
"""
Test module for BaseModel class.
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_base_model(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89

        # Check __str__ method
        self.assertEqual(str(my_model),
                         f"[BaseModel] ({my_model.id}) {my_model.__dict__}")

        # Check save method
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(old_updated_at, my_model.updated_at)

        # Check to_dict method
        my_model_json = my_model.to_dict()
        expected_keys = ['id', 'name',
                         'my_number', '__class__',
                         'created_at', 'updated_at']
        self.assertCountEqual(my_model_json.keys(), expected_keys)


if __name__ == '__main__':
    unittest.main()
