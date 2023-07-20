# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 20/07/23
import unittest
import uuid
from unittest.mock import MagicMock

from app.stuquiz.entities.professor import Professor
from app.stuquiz.repositories.professor_repository import ProfessorRepository


class TestProfessorRepository(unittest.TestCase):
    TEST_PROFESSOR = Professor(str(uuid.uuid4()), 'Professor name')

    def setUp(self) -> None:
        self.cursor = MagicMock()
        self.db = MagicMock()
        self.db_provider = MagicMock()

        self.db.cursor.return_value = self.cursor
        self.db_provider.get_db.return_value = self.db
        self.repository = ProfessorRepository(self.db_provider)

    def tearDown(self) -> None:
        self.cursor = None
        self.db = None
        self.db_provider = None
        self.repository = None

    def testCreateProfessor_ReturnTrue_WhenProfessorCreated(self):
        # Arrange
        expected_query = 'INSERT INTO professor(id, name) VALUES(%s, %s)'
        expected_args = (self.TEST_PROFESSOR.id, self.TEST_PROFESSOR.name)

        # Act
        result = self.repository.create_professor(self.TEST_PROFESSOR)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_args)
        self.db.commit.assert_called_once()
        self.assertTrue(result)

    def testUpdateProfessor_ReturnTrue_WhenProfessorUpdated(self):
        # Arrange
        expected_query = 'UPDATE professor SET name = %s WHERE id = %s'
        expected_args = (self.TEST_PROFESSOR.name, self.TEST_PROFESSOR.id)

        # Act
        result = self.repository.update_professor(self.TEST_PROFESSOR)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_args)
        self.db.commit.assert_called_once()
        self.assertTrue(result)

    def testDeleteProfessor_ReturnTrue_WhenProfessorDeleted(self):
        # Arrange
        expected_query = 'DELETE FROM professor WHERE id = %s'
        expected_args = (self.TEST_PROFESSOR.id,)

        # Act
        result = self.repository.delete_professor(self.TEST_PROFESSOR)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_args)
        self.db.commit.assert_called_once()
        self.assertTrue(result)

    def testSelectProfessorById_ReturnProfessor_WhenProfessorExist(self):
        # Arrange
        expected_query = 'SELECT id, name FROM professor WHERE id = %s'
        expected_args = (self.TEST_PROFESSOR.id,)
        self.cursor.fetchall.return_value = [(self.TEST_PROFESSOR.id, self.TEST_PROFESSOR.name)]

        # Act
        result = self.repository.select_professor_by_id(self.TEST_PROFESSOR.id)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_args)
        self.assertEqual(self.TEST_PROFESSOR, result)

    def testSelectProfessorById_ReturnNone_WhenProfessorDontExist(self):
        # Arrange
        expected_query = 'SELECT id, name FROM professor WHERE id = %s'
        expected_args = (self.TEST_PROFESSOR.id,)
        self.cursor.fetchall.return_value = None

        # Act
        result = self.repository.select_professor_by_id(self.TEST_PROFESSOR.id)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_args)
        self.assertIsNone(result)

    def testSelectProfessors_ReturnProfessorList_WhenProfessorsExist(self):
        # Arrange
        professor1 = Professor(str(uuid.uuid4()), 'Professor 1')
        professor2 = Professor(str(uuid.uuid4()), 'Professor 2')
        expected_query = 'SELECT id, name FROM professor'
        expected_args = ()
        expected_result = [professor1, professor2]
        self.cursor.fetchall.return_value = [(professor1.id, professor1.name), (professor2.id, professor2.name)]

        # Act
        result = self.repository.select_professors()

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_args)
        self.assertEqual(expected_result, result)

    def testSelectProfessors_ReturnEmptyList_WhenProfessorsDontExist(self):
        # Arrange
        expected_query = 'SELECT id, name FROM professor'
        expected_args = ()
        expected_result = []
        self.cursor.fetchall.return_value = []

        # Act
        result = self.repository.select_professors()

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_args)
        self.assertEqual(expected_result, result)
