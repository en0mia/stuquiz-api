# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 12/07/23
import json
import unittest
import uuid
from unittest import mock
from unittest.mock import MagicMock

from app.stuquiz.controllers.university.update_university_controller import UpdateUniversityController
from app.stuquiz.entities.university import University


class TestUpdateUniversityController(unittest.TestCase):
    TEST_UNIVERSITY = University(str(uuid.uuid4()), 'University Name')
    TEST_NEW_NAME = 'New Name'

    def setUp(self) -> None:
        self.request = MagicMock()
        self.university_model = MagicMock()
        self.admin_model = MagicMock()
        self.controller = UpdateUniversityController(self.university_model, self.admin_model)
        self.args = mock.PropertyMock(return_value={'university_id': self.TEST_UNIVERSITY.id})
        self.form = mock.PropertyMock(return_value={'name': self.TEST_NEW_NAME})
        type(self.request).args = self.args
        type(self.request).form = self.form

    def tearDown(self) -> None:
        self.request = None
        self.university_model = None
        self.admin_model = None
        self.controller = None
        self.args = None
        self.form = None

    def testExecute_return404_whenUniversityDoesNotExist(self):
        # Arrange
        self.university_model.get_university_by_id.return_value = None

        # Act
        result = self.controller.execute(self.request)

        # Assert
        self.args.assert_called_once()
        self.form.assert_not_called()
        self.university_model.update_university.assert_not_called()
        self.assertEqual(404, result.status_code)

    def testExecute_return500_whenDbError(self):
        # Arrange
        self.university_model.get_university_by_id.return_value = self.TEST_UNIVERSITY
        self.university_model.update_university.return_value = False

        # Act
        result = self.controller.execute(self.request)

        # Assert
        self.args.assert_called_once()
        self.form.assert_called_once()
        self.university_model.update_university.assert_called_once()
        self.assertEqual(500, result.status_code)

    def testExecute_return200_whenUniversityUpdated(self):
        # Arrange
        self.university_model.get_university_by_id.return_value = self.TEST_UNIVERSITY
        self.university_model.update_university.return_value = True
        new_university = University(self.TEST_UNIVERSITY.id, self.TEST_NEW_NAME)
        expected_body = {}

        # Act
        result = self.controller.execute(self.request)

        # Assert
        self.args.assert_called_once()
        self.form.assert_called_once()
        self.university_model.update_university.assert_called_once_with(new_university)
        self.assertEqual(200, result.status_code)
        self.assertEqual(expected_body, json.loads(result.data))
