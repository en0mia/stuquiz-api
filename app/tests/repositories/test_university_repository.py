# @author Lorenzo Varese
# @created 2023-06-30

import unittest
from unittest.mock import MagicMock

from app.stuquiz.entities.university import University
from app.stuquiz.repositories.university_repository import UniversityRepository
from app.tests.repositories.test_constants import TEST_UNIVERSITY


class TestUniversityRepository(unittest.TestCase):
    TEST_ID = TEST_UNIVERSITY.id
    test_university = TEST_UNIVERSITY

    def setUp(self) -> None:
        self.cursor = MagicMock()
        self.cursor.fetchone.return_value = None  # Mock the return value of fetchone method
        self.db = MagicMock()
        self.db_provider = MagicMock()

        self.db.cursor.return_value = self.cursor
        self.db_provider.get_db.return_value = self.db
        self.repository = UniversityRepository(self.db_provider)

    def tearDown(self) -> None:
        self.cursor = None
        self.db = None
        self.db_provider = None
        self.repository = None

    def test_create_university(self):
        university = University(
            id=self.TEST_ID,
            name='Sample University'
        )

        # Call the create_university method
        result = self.repository.create_university(university)

        # Assert that the insert method was called with the correct query and argument
        expected_query = 'INSERT INTO university (name) VALUES (%s)'
        expected_arg = university.name
        self.cursor.execute.assert_called_once_with(expected_query, expected_arg)

        # Assert that the commit method was called on the database connection
        self.db.commit.assert_called_once()

        # Assert that the result is True, indicating successful creation
        self.assertTrue(result)

    def test_delete_university(self):
        university = University(
            id=self.TEST_ID,
            name='Sample University'
        )

        # Call the delete_university method
        result = self.repository.delete_university(university)

        # Assert that the delete method was called with the correct query and argument
        expected_query = 'DELETE FROM university WHERE id = %s'
        expected_arg = university.id
        self.cursor.execute.assert_called_once_with(expected_query, expected_arg)

        # Assert that the commit method was called on the database connection
        self.db.commit.assert_called_once()

        # Assert that the result is True, indicating successful deletion
        self.assertTrue(result)

    def test_update_university(self):
        university = University(
            id=self.TEST_ID,
            name='Sample University'
        )

        # Call the update_university method
        result = self.repository.update_university(university)

        # Assert that the update method was called with the correct query and arguments
        expected_query = 'UPDATE university SET name = %s WHERE id = %s'
        expected_args = (university.name, university.id)
        self.cursor.execute.assert_called_once_with(expected_query, expected_args)

        # Assert that the commit method was called on the database connection
        self.db.commit.assert_called_once()

        # Assert that the result is True, indicating successful update
        self.assertTrue(result)

    def test_select_university_by_id_when_university_exist(self):
        # Arrange
        expected_result = University(self.test_university.id, self.test_university.name)

        self.cursor.fetchall.return_value = University(self.test_university.id, self.test_university.name)

        # Act
        result = self.repository.select_university_by_id(self.test_university.id)

        # Assert
        self.assertEqual(expected_result, result)

    def test_select_university_by_id_when_university_doesnt_exist(self):
        # Arrange
        self.cursor.fetchall.return_value = None

        # Act
        result = self.repository.select_university_by_id(self.TEST_ID)

        # Assert
        self.assertIsNone(result)
