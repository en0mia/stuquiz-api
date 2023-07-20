# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 20/07/23
import json
import unittest
from unittest.mock import MagicMock

from app.stuquiz.controllers.professor.add_professor_controller import AddProfessorController


class TestAddProfessorController(unittest.TestCase):
    TEST_NAME = 'Professor name'

    def setUp(self) -> None:
        self.professor_model = MagicMock()
        self.admin_model = MagicMock()
        self.controller = AddProfessorController(self.professor_model, self.admin_model)

    def tearDown(self) -> None:
        self.professor_model = None
        self.admin_model = None
        self.controller = None

    def testExecute_return401_whenAdminNotLoggedIn(self):
        # Arrange
        self.admin_model.is_admin_logged_in.return_value = False

        # Act
        result = self.controller.execute({'name': self.TEST_NAME})

        # Assert
        self.admin_model.is_admin_logged_in.assert_called_once()
        self.professor_model.add_professor.assert_not_called()
        self.assertEqual(401, result.status_code)

    def testExecute_return400_whenInvalidProfessorName(self):
        # Arrange
        self.admin_model.is_admin_logged_in.return_value = True

        # Act
        result = self.controller.execute({'name': ''})

        # Assert
        self.admin_model.is_admin_logged_in.assert_called_once()
        self.professor_model.add_professor.assert_not_called()
        self.assertEqual(400, result.status_code)

    def testExecute_return500_whenDbError(self):
        # Arrange
        self.admin_model.is_admin_logged_in.return_value = True
        self.professor_model.add_professor.return_value = False

        # Act
        result = self.controller.execute({'name': self.TEST_NAME})

        # Assert
        self.admin_model.is_admin_logged_in.assert_called_once()
        self.professor_model.add_professor.assert_called_once()
        self.assertEqual(500, result.status_code)

    def testExecute_return200WithEmptyBody_whenProfessorHasBeenAdded(self):
        # Arrange
        expected_body = {}
        self.professor_model.add_professor.return_value = True
        self.admin_model.is_admin_logged_in.return_value = True

        # Act
        result = self.controller.execute({'name': self.TEST_NAME})

        # Assert
        self.admin_model.is_admin_logged_in.assert_called_once()
        self.professor_model.add_professor.assert_called_once()
        self.assertEqual(200, result.status_code)
        self.assertEqual(expected_body, json.loads(result.data))
