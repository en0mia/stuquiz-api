# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 20/07/23
import json
import unittest
import uuid
from unittest.mock import MagicMock

from app.stuquiz.controllers.professor.get_professors_controller import GetProfessorsController
from app.stuquiz.entities.professor import Professor


class TestGetProfessorsController(unittest.TestCase):
    def setUp(self) -> None:
        self.professor_model = MagicMock()
        self.controller = GetProfessorsController(self.professor_model)

    def tearDown(self) -> None:
        self.professor_model = None
        self.controller = None

    def testExecute_return200WithEmptyBody_whenProfessorsDontExist(self):
        # Arrange
        expected_body = []
        self.professor_model.get_professors.return_value = []

        # Act
        result = self.controller.execute({})

        # Assert
        self.professor_model.get_professors.assert_called_once()
        self.assertEqual(200, result.status_code)
        self.assertEqual(expected_body, json.loads(result.data))

    def testExecute_return200_whenProfessorsExist(self):
        # Arrange
        first_professor = Professor(str(uuid.uuid4()), 'First Professor')
        second_professor = Professor(str(uuid.uuid4()), 'Second Professor')
        expected_body = [
            {'id': first_professor.id, 'name': first_professor.name},
            {'id': second_professor.id, 'name': second_professor.name}
        ]
        self.professor_model.get_professors.return_value = [first_professor, second_professor]

        # Act
        result = self.controller.execute({})

        # Assert
        self.professor_model.get_professors.assert_called_once()
        self.assertEqual(200, result.status_code)
        self.assertEqual(expected_body, json.loads(result.data))
