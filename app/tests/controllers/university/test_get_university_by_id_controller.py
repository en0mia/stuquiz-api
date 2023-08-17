# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 04/07/23
import json
import unittest
import uuid
from unittest import mock
from unittest.mock import MagicMock

from app.stuquiz.controllers.university.get_university_by_id_controller import GetUniversityByIdController
from app.stuquiz.entities.university import University


class TestGetUniversitiesController(unittest.TestCase):
    TEST_UNIVERSITY = University(str(uuid.uuid4()), 'Test University')

    def setUp(self) -> None:
        self.university_model = MagicMock()
        self.request = MagicMock()
        self.args = mock.PropertyMock(return_value={'university_id': self.TEST_UNIVERSITY.id})
        type(self.request).args = self.args
        self.controller = GetUniversityByIdController(self.university_model)

    def tearDown(self) -> None:
        self.university_model = None
        self.request = None
        self.controller = None

    def testExecute_return404_whenUniversityDontExist(self):
        # Arrange
        self.university_model.get_university_by_id.return_value = []

        # Act
        result = self.controller.execute(self.request)

        # Assert
        self.args.assert_called_once()
        self.university_model.get_university_by_id.assert_called_once()
        self.assertEqual(404, result.status_code)

    def testExecute_return200_whenUniversityExist(self):
        # Arrange
        expected_body = {'id': self.TEST_UNIVERSITY.id, 'name': self.TEST_UNIVERSITY.name}
        self.university_model.get_university_by_id.return_value = self.TEST_UNIVERSITY

        # Act
        result = self.controller.execute(self.request)

        # Assert
        self.args.assert_called_once()
        self.university_model.get_university_by_id.assert_called_once()
        self.assertEqual(200, result.status_code)
        self.assertEqual(expected_body, json.loads(result.data))
