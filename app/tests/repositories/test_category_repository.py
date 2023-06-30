# @author Lorenzo Varese
# @created 2023-06-30

import unittest
import uuid
from unittest.mock import MagicMock

from app.stuquiz.entities.category import Category
from app.stuquiz.repositories.category_repository import CategoryRepository
from app.tests.repositories.test_constants import TEST_CATEGORY


class TestCategoryRepository(unittest.TestCase):
    TEST_ID = TEST_CATEGORY.id
    test_category = TEST_CATEGORY

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

    def test_create_category(self):
        category = Category(
            id=self.TEST_ID,
            name='Sample Category'
        )

        # Call the create_category method
        result = self.repository.create_category(category)

        # Assert that the insert method was called with the correct query and argument
        expected_query = 'INSERT INTO category (name) VALUES (%s)'
        expected_arg = category.name
        self.cursor.execute.assert_called_once_with(expected_query, expected_arg)

        # Assert that the commit method was called on the database connection
        self.db.commit.assert_called_once()

        # Assert that the result is True, indicating successful creation
        self.assertTrue(result)

    def test_delete_category(self):
        category = Category(
            id=self.TEST_ID,
            name='Sample Category'
        )

        # Call the delete_category method
        result = self.repository.delete_category(category)

        # Assert that the delete method was called with the correct query and argument
        expected_query = 'DELETE FROM category WHERE id = %s'
        expected_arg = category.id
        self.cursor.execute.assert_called_once_with(expected_query, expected_arg)

        # Assert that the commit method was called on the database connection
        self.db.commit.assert_called_once()

        # Assert that the result is True, indicating successful deletion
        self.assertTrue(result)

    def test_update_category(self):
        category = Category(
            id=self.TEST_ID,
            name='Sample Category'
        )

        # Call the update_category method
        result = self.repository.update_category(category)

        # Assert that the update method was called with the correct query and arguments
        expected_query = 'UPDATE category SET name = %s WHERE id = %s'
        expected_args = (category.name, category.id)
        self.cursor.execute.assert_called_once_with(expected_query, expected_args)

        # Assert that the commit method was called on the database connection
        self.db.commit.assert_called_once()

        # Assert that the result is True, indicating successful update
        self.assertTrue(result)

    def test_select_category_by_id_when_category_exists(self):
        # Arrange
        expected_result = Category(self.test_category.id, self.test_category.name)

        self.cursor.fetchall.return_value = expected_result

        # Act
        result = self.repository.select_category_by_id(self.test_category.id)

        # Assert
        self.assertEqual(expected_result, result)

    def test_select_category_by_id_when_category_doesnt_exist(self):
        # Arrange
        self.cursor.fetchall.return_value = None

        # Act
        result = self.repository.select_category_by_id(self.TEST_ID)

        # Assert
        self.assertIsNone(result)
