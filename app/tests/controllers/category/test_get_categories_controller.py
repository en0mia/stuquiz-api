# @author Lorenzo Varese
# @created 2023-07-05


import json
import unittest
import uuid
from unittest.mock import MagicMock

from app.stuquiz.controllers.category.get_categories_controller import GetCategoriesController
from app.stuquiz.entities.category import Category


class TestGetCategoriesController(unittest.TestCase):
    def setUp(self) -> None:
        self.category_model = MagicMock()
        self.controller = GetCategoriesController(self.category_model)

    def tearDown(self) -> None:
        self.category_model = None
        self.controller = None

    def testExecute_return200WithEmptyBody_whenCategoriesDontExist(self):
        # Arrange
        expected_body = []
        self.category_model.get_categories.return_value = []

        # Act
        result = self.controller.execute({})

        # Assert
        self.category_model.get_categories.assert_called_once()
        self.assertEqual(200, result.status_code)
        self.assertEqual(expected_body, json.loads(result.data))

    def testExecute_return200_whenCategoriesExist(self):
        # Arrange
        first_category = Category(str(uuid.uuid4()), 'First Category')
        second_category = Category(str(uuid.uuid4()), 'Second Category')
        expected_body = [
            {'id': first_category.id, 'name': first_category.name},
            {'id': second_category.id, 'name': second_category.name}
        ]
        self.category_model.get_categories.return_value = [first_category, second_category]

        # Act
        result = self.controller.execute({})

        # Assert
        self.category_model.get_categories.assert_called_once()
        self.assertEqual(200, result.status_code)
        self.assertEqual(expected_body, json.loads(result.data))
