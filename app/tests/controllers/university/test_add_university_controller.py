# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 11/07/23
import json
import unittest
from unittest.mock import MagicMock

from app.stuquiz.controllers.university.add_university_controller import AddUniversityController


class TestGetUniversitiesController(unittest.TestCase):
    TEST_NAME = 'University name'

    def setUp(self) -> None:
        self.university_model = MagicMock()
        self.admin_model = MagicMock()
        self.controller = AddUniversityController(self.university_model, self.admin_model)

    def tearDown(self) -> None:
        self.university_model = None
        self.controller = None

    def testExecute_return401_whenAdminNotLoggedIn(self):
        # Arrange
        self.admin_model.is_admin_logged_in.return_value = False

        # Act
        result = self.controller.execute({'name': self.TEST_NAME})

        # Assert
        self.admin_model.is_admin_logged_in.assert_called_once()
        self.university_model.add_university.assert_not_called()
        self.assertEqual(401, result.status_code)

    def testExecute_return400_whenAdminNotLoggedIn(self):
        # Arrange

        # Act
        result = self.controller.execute({'name': ''})

        # Assert
        self.admin_model.is_admin_logged_in.assert_called_once()
        self.university_model.add_university.assert_not_called()
        self.assertEqual(400, result.status_code)

    def testExecute_return500_whenDbError(self):
        # Arrange
        self.admin_model.is_admin_logged_in.return_value = True
        self.university_model.add_university.return_value = False

        # Act
        result = self.controller.execute({'name': self.TEST_NAME})

        # Assert
        self.admin_model.is_admin_logged_in.assert_called_once()
        self.university_model.add_university.assert_called_once()
        self.assertEqual(500, result.status_code)

    def testExecute_return200WithEmptyBody_whenUniversityHasBeenAdded(self):
        # Arrange
        expected_body = {}
        self.university_model.add_university.return_value = True
        self.admin_model.is_admin_logged_in.return_value = True

        # Act
        result = self.controller.execute({'name': self.TEST_NAME})

        # Assert
        self.admin_model.is_admin_logged_in.assert_called_once()
        self.university_model.add_university.assert_called_once()
        self.assertEqual(200, result.status_code)
        self.assertEqual(expected_body, json.loads(result.data))
