# @author Lorenzo Varese
# @created 2023-07-05


import json
import unittest
import uuid
from unittest.mock import MagicMock

from app.stuquiz.controllers.category.get_category_by_id_controller import GetCategoryByIdController
from app.stuquiz.entities.category import Category


class TestGetCategoriesByIdController(unittest.TestCase):
    TEST_CATEGORY = Category(str(uuid.uuid4()), 'Test Category')

    def setUp(self) -> None:
        self.category_model = MagicMock()
        self.controller = GetCategoryByIdController(self.category_model)

    def tearDown(self) -> None:
        self.category_model = None
        self.controller = None

    def testExecute_return404_whenCategoryDontExist(self):
        # Arrange
        expected_body = []
        self.category_model.get_category_by_id.return_value = []

        # Act
        result = self.controller.execute({'category_id': str(uuid.uuid4())})

        # Assert
        self.category_model.get_category_by_id.assert_called_once()
        self.assertEqual(404, result.status_code)

    def testExecute_return200_whenCategoryExist(self):
        # Arrange
        expected_body = {'id': self.TEST_CATEGORY.id, 'name': self.TEST_CATEGORY.name}
        self.category_model.get_category_by_id.return_value = self.TEST_CATEGORY

        # Act
        result = self.controller.execute({'category_id': self.TEST_CATEGORY.id})

        # Assert
        self.category_model.get_category_by_id.assert_called_once()
        self.assertEqual(200, result.status_code)
        self.assertEqual(expected_body, json.loads(result.data))

    def testExecute_return400_whenCategoryIdIsNotValid(self):
        # Arrange

        # Act
        result = self.controller.execute({'category_id': None})

        # Assert
        self.category_model.get_category_by_id.assert_not_called()
        self.assertEqual(400, result.status_code)
