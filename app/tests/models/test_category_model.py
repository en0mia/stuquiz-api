# @author Lorenzo Varese
# @created 2023-06-30


import unittest
from unittest.mock import MagicMock

from app.stuquiz.models.category.category_model import CategoryModel


class TestCategoryModel(unittest.TestCase):
    def setUp(self) -> None:
        self.category_repository = MagicMock()
        self.model = CategoryModel(self.category_repository)

    def tearDown(self) -> None:
        self.category_repository = None
        self.model = None

    def testGetCategories_callRepository_whenCalled(self):
        # Arrange
        self.category_repository.select_categories.return_value = []

        # Act
        self.model.get_categories()

        # Assert
        self.category_repository.select_categories.assert_called_once()

    def testGetCategoriesById_callRepository_whenCalled(self):
        # Arrange
        self.category_repository.select_category_by_id.return_value = []

        # Act
        self.model.get_category_by_id('')

        # Assert
        self.category_repository.select_category_by_id.assert_called_once()
