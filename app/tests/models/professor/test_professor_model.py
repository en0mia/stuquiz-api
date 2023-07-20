# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 20/07/23
import unittest
import uuid
from unittest.mock import MagicMock

from app.stuquiz.entities.professor import Professor
from app.stuquiz.models.professor.professor_model import ProfessorModel


class TestProfessorModel(unittest.TestCase):
    def setUp(self) -> None:
        self.professor_repository = MagicMock()
        self.professor_model = ProfessorModel(self.professor_repository)

    def tearDown(self) -> None:
        self.professor_repository = None
        self.professor_model = None

    def testGetProfessors_callRepository_whenCalled(self):
        # Arrange
        self.professor_repository.select_professors.return_value = []

        # Act
        self.professor_model.get_professors()

        # Assert
        self.professor_repository.select_professors.assert_called_once()

    def testGetProfessorById_callRepository_whenCalled(self):
        # Arrange
        self.professor_repository.select_professor_by_id.return_value = []

        # Act
        self.professor_model.get_professor_by_id(str(uuid.uuid4()))

        # Assert
        self.professor_repository.select_professor_by_id.assert_called_once()

    def testAddProfessor_callRepository_whenCalled(self):
        # Arrange
        self.professor_repository.create_professor.return_value = True

        # Act
        self.professor_model.add_professor('Professor name')

        # Assert
        self.professor_repository.create_professor.assert_called_once()

    def testUpdateProfessor_callRepository_whenCalled(self):
        # Arrange
        professor = Professor(str(uuid.uuid4()), 'Professor name')
        self.professor_repository.update_professor.return_value = True

        # Act
        self.professor_model.update_professor(professor)

        # Assert
        self.professor_repository.update_professor.assert_called_once()
