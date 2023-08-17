# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 11/07/23
import json
import unittest
from unittest import mock
from unittest.mock import MagicMock

from app.stuquiz.controllers.university.add_university_controller import AddUniversityController


class TestAddUniversityController(unittest.TestCase):
    TEST_NAME = 'University name'

    def setUp(self) -> None:
        self.request = MagicMock()
        self.university_model = MagicMock()
        self.admin_model = MagicMock()
        self.controller = AddUniversityController(self.university_model)
        self.form = mock.PropertyMock(return_value={'name': self.TEST_NAME})
        type(self.request).form = self.form

    def tearDown(self) -> None:
        self.request = None
        self.university_model = None
        self.admin_model = None
        self.controller = None
        self.form = None

    def testExecute_return500_whenDbError(self):
        # Arrange
        self.university_model.add_university.return_value = False

        # Act
        result = self.controller.execute(self.request)

        # Assert
        self.form.assert_called_once()
        self.university_model.add_university.assert_called_once()
        self.assertEqual(500, result.status_code)

    def testExecute_return200WithEmptyBody_whenUniversityHasBeenAdded(self):
        # Arrange
        expected_body = {}
        self.university_model.add_university.return_value = True

        # Act
        result = self.controller.execute(self.request)

        # Assert
        self.form.assert_called_once()
        self.university_model.add_university.assert_called_once()
        self.assertEqual(200, result.status_code)
        self.assertEqual(expected_body, json.loads(result.data))
