# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 20/07/23
import unittest
from unittest.mock import MagicMock

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
