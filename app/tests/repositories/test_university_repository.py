# @author Lorenzo Varese
# @created 2023-06-30

import unittest
import uuid
from unittest.mock import MagicMock

from app.stuquiz.entities.university import University
from app.stuquiz.repositories.university_repository import UniversityRepository


class TestUniversityRepository(unittest.TestCase):
    TEST_UNIVERSITY = University(str(uuid.uuid4()), "Test University")

    def setUp(self) -> None:
        self.cursor = MagicMock()
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

    def testCreateUniversity_ReturnTrue_WhenUniversityCreated(self):
        # Arrange
        expected_query = 'INSERT INTO university (name) VALUES (%s)'
        expected_arg = (self.TEST_UNIVERSITY.name, )

        # Act
        result = self.repository.create_university(self.TEST_UNIVERSITY)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_arg)
        self.db.commit.assert_called_once()
        self.assertTrue(result)

    def testDeleteUniversity_ReturnTrue_WhenUniversityDeleted(self):
        # Arrange
        expected_query = 'DELETE FROM university WHERE id = %s'
        expected_arg = (self.TEST_UNIVERSITY.id, )

        # Act
        result = self.repository.delete_university(self.TEST_UNIVERSITY)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_arg)
        self.db.commit.assert_called_once()
        self.assertTrue(result)

    def testUpdateUniversity_ReturnTrue_WhenUniversityUpdated(self):
        # Arrange
        expected_query = 'UPDATE university SET name = %s WHERE id = %s'
        expected_args = (self.TEST_UNIVERSITY.name, self.TEST_UNIVERSITY.id)

        # Act
        result = self.repository.update_university(self.TEST_UNIVERSITY)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_args)
        self.db.commit.assert_called_once()
        self.assertTrue(result)

    def testSelectUniversityById_ReturnUniversity_WhenUniversityExist(self):
        # Arrange
        expected_result = University(self.TEST_UNIVERSITY.id, self.TEST_UNIVERSITY.name)

        self.cursor.fetchall.return_value = [(self.TEST_UNIVERSITY.id, self.TEST_UNIVERSITY.name)]

        # Act
        result = self.repository.select_university_by_id(self.TEST_UNIVERSITY.id)

        # Assert
        self.assertEqual(expected_result, result)

    def testSelectUniversityById_ReturnNone_WhenUniversityDontExist(self):
        # Arrange
        self.cursor.fetchall.return_value = None

        # Act
        result = self.repository.select_university_by_id("test-id")

        # Assert
        self.assertIsNone(result)

    def test_selectUniversities_returnUniversities_whenUniversitiesExist(self):
        # Arrange
        first_university = (self.TEST_UNIVERSITY.id, self.TEST_UNIVERSITY.name)
        second_university = (uuid.uuid4(), self.TEST_UNIVERSITY.name + "second")
        return_value = [first_university, second_university]
        self.cursor.fetchall.return_value = return_value
        expected_result = [University(*first_university), University(*second_university)]

        # Act
        result = self.repository.select_universities()

        # Assert
        self.assertEqual(expected_result, result)
        self.cursor.execute.assert_called_once_with('SELECT id, name FROM university;', ())

    def test_selectUniversities_returnEmptyList_whenUniversitiesDontExist(self):
        # Arrange
        return_value = []
        self.cursor.fetchall.return_value = return_value

        # Act
        result = self.repository.select_universities()

        # Assert
        self.assertEqual([], result)
        self.cursor.execute.assert_called_once_with('SELECT id, name FROM university;', ())

    def test_selectUniversities_returnEmptyList_whenDbError(self):
        # Arrange
        return_value = None
        self.cursor.fetchall.return_value = return_value

        # Act
        result = self.repository.select_universities()

        # Assert
        self.assertEqual([], result)
        self.cursor.execute.assert_called_once_with('SELECT id, name FROM university;', ())
