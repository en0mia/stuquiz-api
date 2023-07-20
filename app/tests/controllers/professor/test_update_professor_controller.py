# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 20/07/23
import json
import unittest
import uuid
from unittest.mock import MagicMock

from app.stuquiz.controllers.professor.update_professor_controller import UpdateProfessorController
from app.stuquiz.entities.professor import Professor


class TestUpdateProfessorController(unittest.TestCase):
    TEST_PROFESSOR = Professor(str(uuid.uuid4()), 'Professor Name')

    def setUp(self) -> None:
        self.professor_model = MagicMock()
        self.admin_model = MagicMock()
        self.controller = UpdateProfessorController(self.professor_model, self.admin_model)

    def tearDown(self) -> None:
        self.professor_model = None
        self.admin_model = None
        self.controller = None

    def testExecute_return401_whenAdminNotLoggedIn(self):
        # Arrange
        self.admin_model.is_admin_logged_in.return_value = False

        # Act
        result = self.controller.execute({'professor_id': self.TEST_PROFESSOR.id, 'name': self.TEST_PROFESSOR.name})

        # Assert
        self.admin_model.is_admin_logged_in.assert_called_once()
        self.professor_model.update_professor.assert_not_called()
        self.assertEqual(401, result.status_code)

    def testExecute_return400_whenInvalidParameters(self):
        # Arrange
        self.admin_model.is_admin_logged_in.return_value = True

        # Act
        result = self.controller.execute({'professor_id': 'invalid id', 'name': ''})

        # Assert
        self.admin_model.is_admin_logged_in.assert_called_once()
        self.professor_model.update_professor.assert_not_called()
        self.assertEqual(400, result.status_code)

    def testExecute_return404_whenProfessorDontExist(self):
        # Arrange
        self.admin_model.is_admin_logged_in.return_value = True
        self.professor_model.get_professor_by_id.return_value = None

        # Act
        result = self.controller.execute({'professor_id': self.TEST_PROFESSOR.id, 'name': self.TEST_PROFESSOR.name})

        # Assert
        self.admin_model.is_admin_logged_in.assert_called_once()
        self.professor_model.update_professor.assert_not_called()
        self.professor_model.get_professor_by_id.assert_called_once()
        self.assertEqual(404, result.status_code)

    def testExecute_return500_whenDbError(self):
        # Arrange
        self.admin_model.is_admin_logged_in.return_value = True
        self.professor_model.update_professor.return_value = False

        # Act
        result = self.controller.execute({'professor_id': self.TEST_PROFESSOR.id, 'name': self.TEST_PROFESSOR.name})

        # Assert
        self.admin_model.is_admin_logged_in.assert_called_once()
        self.professor_model.update_professor.assert_called_once()
        self.assertEqual(500, result.status_code)

    def testExecute_return200WithEmptyBody_whenProfessorHasBeenUpdated(self):
        # Arrange
        expected_body = {}
        self.professor_model.update_professor.return_value = True
        self.admin_model.is_admin_logged_in.return_value = True

        # Act
        result = self.controller.execute({'professor_id': self.TEST_PROFESSOR.id, 'name': self.TEST_PROFESSOR.name})

        # Assert
        self.admin_model.is_admin_logged_in.assert_called_once()
        self.professor_model.update_professor.assert_called_once()
        self.assertEqual(200, result.status_code)
        self.assertEqual(expected_body, json.loads(result.data))
