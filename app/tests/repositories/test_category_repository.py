# @author Lorenzo Varese
# @created 2023-06-30

import unittest
import uuid
from unittest.mock import MagicMock

from app.stuquiz.entities.category import Category
from app.stuquiz.repositories.category_repository import CategoryRepository


class TestCategoryRepository(unittest.TestCase):
    test_category = None
    NON_EXISTING_ID = 'id-test'

    def setUp(self) -> None:
        self.cursor = MagicMock()
        self.db = MagicMock()
        self.db_provider = MagicMock()

        self.db.cursor.return_value = self.cursor
        self.db_provider.get_db.return_value = self.db
        self.repository = CategoryRepository(self.db_provider)

        self.test_category = Category(
            id=str(uuid.uuid4()),
            name="Test category"
        )

    def tearDown(self) -> None:
        self.cursor = None
        self.db = None
        self.db_provider = None
        self.repository = None
        self.test_category = None

    def test_create_category(self):
        # Arrange
        expected_query = 'INSERT INTO category (name) VALUES (%s)'
        expected_arg = (self.test_category.name, )

        # Act
        result = self.repository.create_category(self.test_category)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_arg)

        self.db.commit.assert_called_once()

        self.assertTrue(result)

    def test_delete_category(self):
        # Arrange
        expected_query = 'DELETE FROM category WHERE id = %s'
        expected_arg = (self.test_category.id, )

        # Act
        result = self.repository.delete_category(self.test_category)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_arg)

        self.db.commit.assert_called_once()

        self.assertTrue(result)

    def test_update_category(self):
        # Arrange
        expected_query = 'UPDATE category SET name = %s WHERE id = %s'
        expected_args = (self.test_category.name, self.test_category.id)

        # Act
        result = self.repository.update_category(self.test_category)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_args)

        self.db.commit.assert_called_once()

        self.assertTrue(result)

    def test_select_category_by_id_when_category_exists(self):
        # Arrange
        self.cursor.fetchall.return_value = [(self.test_category.id, self.test_category.name)]
        expected_result = Category(self.test_category.id, self.test_category.name)
        expected_query = 'SELECT id, name FROM category WHERE id = %s'
        expected_arg = (self.test_category.id, )

        # Act
        result = self.repository.select_category_by_id(self.test_category.id)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_arg)
        self.assertEqual(expected_result, result)

    def test_select_category_by_id_when_category_doesnt_exist(self):
        # Arrange
        self.cursor.fetchall.return_value = None
        expected_query = 'SELECT id, name FROM category WHERE id = %s'
        expected_arg = (self.NON_EXISTING_ID, )

        # Act
        result = self.repository.select_category_by_id(self.NON_EXISTING_ID)
        self.cursor.execute.assert_called_once_with(expected_query, expected_arg)

        # Assert
        self.assertIsNone(result)
