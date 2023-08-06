# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 16/07/23
import json
import unittest
import uuid
from unittest import mock
from unittest.mock import MagicMock

from app.stuquiz.controllers.university.delete_university_controller import DeleteUniversityController
from app.stuquiz.entities.university import University


class TestDeleteUniversityController(unittest.TestCase):
    TEST_UNIVERSITY = University(str(uuid.uuid4()), 'University Name')

    def setUp(self) -> None:
        self.request = MagicMock()
        self.university_model = MagicMock()
        self.controller = DeleteUniversityController(self.university_model)
        self.args = mock.PropertyMock(return_value={'university_id': self.TEST_UNIVERSITY.id})
        type(self.request).args = self.args

    def tearDown(self) -> None:
        self.request = None
        self.university_model = None
        self.controller = None
        self.args = None

    def testExecute_return404_whenUniversityDoesNotExist(self):
        # Arrange
        self.university_model.get_university_by_id.return_value = None

        # Act
        result = self.controller.execute(self.request)

        # Assert
        self.args.assert_called_once()
        self.university_model.delete_university.assert_not_called()
        self.assertEqual(404, result.status_code)

    def testExecute_return500_whenDbError(self):
        # Arrange
        self.university_model.get_university_by_id.return_value = self.TEST_UNIVERSITY
        self.university_model.delete_university.return_value = False

        # Act
        result = self.controller.execute(self.request)

        # Assert
        self.args.assert_called_once()
        self.university_model.delete_university.assert_called_once()
        self.assertEqual(500, result.status_code)

    def testExecute_return200_whenUniversityDeleted(self):
        # Arrange
        self.university_model.get_university_by_id.return_value = self.TEST_UNIVERSITY
        self.university_model.delete_university.return_value = True
        expected_body = {}

        # Act
        result = self.controller.execute(self.request)

        # Assert
        self.args.assert_called_once()
        self.university_model.delete_university.assert_called_once_with(self.TEST_UNIVERSITY)
        self.assertEqual(200, result.status_code)
        self.assertEqual(expected_body, json.loads(result.data))
