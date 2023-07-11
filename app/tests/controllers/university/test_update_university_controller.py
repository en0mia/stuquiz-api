# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 12/07/23
import json
import unittest
import uuid
from unittest.mock import MagicMock

from app.stuquiz.controllers.university.update_university_controller import UpdateUniversityController
from app.stuquiz.entities.university import University


class TestUpdateUniversityController(unittest.TestCase):
    TEST_UNIVERSITY = University(str(uuid.uuid4()), 'University Name')
    TEST_NEW_NAME = 'New Name'

    def setUp(self) -> None:
        self.university_model = MagicMock()
        self.admin_model = MagicMock()
        self.controller = UpdateUniversityController(self.university_model, self.admin_model)

    def tearDown(self) -> None:
        self.university_model = None
        self.admin_model = None
        self.controller = None

    def testExecute_return401_whenAdminNotLoggedIn(self):
        # Arrange
        self.admin_model.is_admin_logged_in.return_value = False

        # Act
        result = self.controller.execute({'name': self.TEST_UNIVERSITY.name, 'university_id': self.TEST_UNIVERSITY.id})

        # Assert
        self.admin_model.is_admin_logged_in.assert_called_once()
        self.university_model.update_university.assert_not_called()
        self.assertEqual(401, result.status_code)

    def testExecute_return400_whenInvalidUniversityName(self):
        # Arrange
        self.admin_model.is_admin_logged_in.return_value = True

        # Act
        result = self.controller.execute({'name': '', 'university_id': self.TEST_UNIVERSITY.id})

        # Assert
        self.admin_model.is_admin_logged_in.assert_called_once()
        self.university_model.update_university.assert_not_called()
        self.assertEqual(400, result.status_code)

    def testExecute_return400_whenEmptyUniversityId(self):
        # Arrange
        self.admin_model.is_admin_logged_in.return_value = True

        # Act
        result = self.controller.execute({'name': self.TEST_UNIVERSITY.name, 'university_id': ''})

        # Assert
        self.admin_model.is_admin_logged_in.assert_called_once()
        self.university_model.update_university.assert_not_called()
        self.assertEqual(400, result.status_code)

    def testExecute_return400_whenInvalidUniversityId(self):
        # Arrange
        self.admin_model.is_admin_logged_in.return_value = True

        # Act
        result = self.controller.execute({'name': self.TEST_UNIVERSITY.name, 'university_id': 'invalid university id'})

        # Assert
        self.admin_model.is_admin_logged_in.assert_called_once()
        self.university_model.update_university.assert_not_called()
        self.assertEqual(400, result.status_code)

    def testExecute_return400_whenUniversityDoesNotExist(self):
        # Arrange
        self.admin_model.is_admin_logged_in.return_value = True
        self.university_model.get_university_by_id.return_value = None

        # Act
        result = self.controller.execute({'name': self.TEST_UNIVERSITY.name, 'university_id': self.TEST_UNIVERSITY.id})

        # Assert
        self.admin_model.is_admin_logged_in.assert_called_once()
        self.university_model.update_university.assert_not_called()
        self.assertEqual(400, result.status_code)

    def testExecute_return500_whenDbError(self):
        # Arrange
        self.admin_model.is_admin_logged_in.return_value = True
        self.university_model.get_university_by_id.return_value = self.TEST_UNIVERSITY
        self.university_model.update_university.return_value = False

        # Act
        result = self.controller.execute({'name': self.TEST_UNIVERSITY.name, 'university_id': self.TEST_UNIVERSITY.id})

        # Assert
        self.admin_model.is_admin_logged_in.assert_called_once()
        self.university_model.update_university.assert_called_once()
        self.assertEqual(500, result.status_code)

    def testExecute_return200_whenUniversityUpdated(self):
        # Arrange
        self.admin_model.is_admin_logged_in.return_value = True
        self.university_model.get_university_by_id.return_value = self.TEST_UNIVERSITY
        self.university_model.update_university.return_value = True
        new_university = University(self.TEST_UNIVERSITY.id, self.TEST_NEW_NAME)
        expected_body = {}

        # Act
        result = self.controller.execute({'name': self.TEST_NEW_NAME, 'university_id': self.TEST_UNIVERSITY.id})

        # Assert
        self.admin_model.is_admin_logged_in.assert_called_once()
        self.university_model.update_university.assert_called_once_with(new_university)
        self.assertEqual(200, result.status_code)
        self.assertEqual(expected_body, json.loads(result.data))
