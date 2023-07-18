# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 04/07/23
import json
import unittest
import uuid
from unittest.mock import MagicMock

from app.stuquiz.controllers.university.get_universities_controller import GetUniversitiesController
from app.stuquiz.entities.university import University


class TestGetUniversitiesController(unittest.TestCase):
    def setUp(self) -> None:
        self.university_model = MagicMock()
        self.controller = GetUniversitiesController(self.university_model)

    def tearDown(self) -> None:
        self.university_model = None
        self.controller = None

    def testExecute_return200WithEmptyBody_whenUniversitiesDontExist(self):
        # Arrange
        expected_body = []
        self.university_model.get_universities.return_value = []

        # Act
        result = self.controller.execute({})

        # Assert
        self.university_model.get_universities.assert_called_once()
        self.assertEqual(200, result.status_code)
        self.assertEqual(expected_body, json.loads(result.data))

    def testExecute_return200_whenUniversitiesExist(self):
        # Arrange
        first_university = University(str(uuid.uuid4()), 'First University')
        second_university = University(str(uuid.uuid4()), 'Second University')
        expected_body = [
            {'id': first_university.id, 'name': first_university.name},
            {'id': second_university.id, 'name': second_university.name}
        ]
        self.university_model.get_universities.return_value = [first_university, second_university]

        # Act
        result = self.controller.execute({})

        # Assert
        self.university_model.get_universities.assert_called_once()
        self.assertEqual(200, result.status_code)
        self.assertEqual(expected_body, json.loads(result.data))
