# @author Lorenzo Varese
# @created 2023-06-30

import unittest
import uuid
from unittest.mock import MagicMock

from app.stuquiz.entities.category import Category
from app.stuquiz.repositories.category_repository import CategoryRepository


class TestCategoryRepository(unittest.TestCase):
    TEST_CATEGORY = Category(str(uuid.uuid4()), "Test category")

    def setUp(self) -> None:
        self.cursor = MagicMock()
        self.db = MagicMock()
        self.db_provider = MagicMock()

        self.db.cursor.return_value = self.cursor
        self.db_provider.get_db.return_value = self.db
        self.repository = CategoryRepository(self.db_provider)

    def tearDown(self) -> None:
        self.cursor = None
        self.db = None
        self.db_provider = None
        self.repository = None

    def testCreateCategory_ReturnTrue_WhenCategoryCreated(self):
        # Arrange
        expected_query = 'INSERT INTO category (name) VALUES (%s)'
        expected_arg = (self.TEST_CATEGORY.name, )

        # Act
        result = self.repository.create_category(self.TEST_CATEGORY)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_arg)
        self.db.commit.assert_called_once()
        self.assertTrue(result)

    def testDeleteCategory_ReturnTrue_WhenCategoryDeleted(self):
        # Arrange
        expected_query = 'DELETE FROM category WHERE id = %s'
        expected_arg = (self.TEST_CATEGORY.id, )

        # Act
        result = self.repository.delete_category(self.TEST_CATEGORY)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_arg)
        self.db.commit.assert_called_once()
        self.assertTrue(result)

    def testUpdateCategory_ReturnTrue_WhenCategoryUpdated(self):
        # Arrange
        expected_query = 'UPDATE category SET name = %s WHERE id = %s'
        expected_args = (self.TEST_CATEGORY.name, self.TEST_CATEGORY.id)

        # Act
        result = self.repository.update_category(self.TEST_CATEGORY)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_args)
        self.db.commit.assert_called_once()
        self.assertTrue(result)

    def testSelectCategoryById_ReturnCategory_WhenCategoryExist(self):
        # Arrange
        expected_result = Category(self.TEST_CATEGORY.id, self.TEST_CATEGORY.name)
        self.cursor.fetchall.return_value = [(self.TEST_CATEGORY.id, self.TEST_CATEGORY.name)]

        # Act
        result = self.repository.select_category_by_id(self.TEST_CATEGORY.id)

        # Assert
        self.assertEqual(expected_result, result)

    def testSelectCategoryById_ReturnNone_WhenCategoryDontExist(self):
        # Arrange
        self.cursor.fetchall.return_value = None

        # Act
        result = self.repository.select_category_by_id("id-test")

        # Assert
        self.assertIsNone(result)
