# @author Lorenzo Varese
# @created 2023-06-30

import unittest
import uuid
from unittest.mock import MagicMock

from app.stuquiz.entities.university import University
from app.stuquiz.repositories.university_repository import UniversityRepository


class TestUniversityRepository(unittest.TestCase):
    test_university = None

    def setUp(self) -> None:
        self.cursor = MagicMock()
        self.db = MagicMock()
        self.db_provider = MagicMock()

        self.db.cursor.return_value = self.cursor
        self.db_provider.get_db.return_value = self.db
        self.repository = UniversityRepository(self.db_provider)

        self.test_university = University(
            id=str(uuid.uuid4()),
            name="Test University"
        )

    def tearDown(self) -> None:
        self.cursor = None
        self.db = None
        self.db_provider = None
        self.repository = None
        self.test_university = None

    def test_create_university(self):
        # Arrange
        expected_query = 'INSERT INTO university (name) VALUES (%s)'
        expected_arg = self.test_university.name

        # Act
        result = self.repository.create_university(self.test_university)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_arg)

        self.db.commit.assert_called_once()

        self.assertTrue(result)

    def test_delete_university(self):
        # Arrange
        expected_query = 'DELETE FROM university WHERE id = %s'
        expected_arg = self.test_university.id

        # Act
        result = self.repository.delete_university(self.test_university)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_arg)

        self.db.commit.assert_called_once()

        self.assertTrue(result)

    def test_update_university(self):
        # Arrange
        expected_query = 'UPDATE university SET name = %s WHERE id = %s'
        expected_args = (self.test_university.name, self.test_university.id)

        # Act
        result = self.repository.update_university(self.test_university)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_args)

        self.db.commit.assert_called_once()

        self.assertTrue(result)

    def test_select_university_by_id_when_university_exist(self):
        # Arrange
        expected_result = University(self.test_university.id, self.test_university.name)

        self.cursor.fetchall.return_value = [(self.test_university.id, self.test_university.name)]

        # Act
        result = self.repository.select_university_by_id(self.test_university.id)

        # Assert
        self.assertEqual(expected_result, result)

    def test_select_university_by_id_when_university_doesnt_exist(self):
        # Arrange
        self.cursor.fetchall.return_value = None

        # Act
        result = self.repository.select_university_by_id("test-id")

        # Assert
        self.assertIsNone(result)
