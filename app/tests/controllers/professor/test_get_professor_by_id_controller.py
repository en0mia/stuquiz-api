# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 20/07/23
import json
import unittest
import uuid
from unittest.mock import MagicMock

from app.stuquiz.controllers.professor.get_professor_by_id_controller import GetProfessorByIdController
from app.stuquiz.entities.professor import Professor


class TestGetProfessorByIdController(unittest.TestCase):
    TEST_PROFESSOR = Professor(str(uuid.uuid4()), 'Professor Name')

    def setUp(self) -> None:
        self.professor_model = MagicMock()
        self.controller = GetProfessorByIdController(self.professor_model)

    def tearDown(self) -> None:
        self.professor_model = None
        self.controller = None

    def testExecute_return400_whenInvalidProfessorId(self):
        # Arrange

        # Act
        result = self.controller.execute({'professor_id': 'invalid id'})

        # Assert
        self.professor_model.get_professor_by_id.assert_not_called()
        self.assertEqual(400, result.status_code)

    def testExecute_return404_whenProfessorDontExist(self):
        # Arrange
        self.professor_model.get_professor_by_id.return_value = None

        # Act
        result = self.controller.execute({'professor_id': str(uuid.uuid4())})

        # Assert
        self.professor_model.get_professor_by_id.assert_called_once()
        self.assertEqual(404, result.status_code)

    def testExecute_return200_whenProfessorExist(self):
        # Arrange
        expected_body = {'id': self.TEST_PROFESSOR.id, 'name': self.TEST_PROFESSOR.name}
        self.professor_model.get_professor_by_id.return_value = self.TEST_PROFESSOR

        # Act
        result = self.controller.execute({'professor_id': self.TEST_PROFESSOR.id})

        # Assert
        self.professor_model.get_professor_by_id.assert_called_once()
        self.assertEqual(200, result.status_code)
        self.assertEqual(expected_body, json.loads(result.data))
