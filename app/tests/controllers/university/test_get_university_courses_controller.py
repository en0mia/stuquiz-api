# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 16/07/23
import json
import unittest
import uuid
from unittest.mock import MagicMock

from app.stuquiz.controllers.university.get_university_courses_controller import GetUniversityCoursesController
from app.stuquiz.entities.category import Category
from app.stuquiz.entities.course import Course
from app.stuquiz.entities.university import University


class TestGetUniversityCoursesController(unittest.TestCase):
    def setUp(self) -> None:
        self.university_model = MagicMock()
        self.controller = GetUniversityCoursesController(self.university_model)

    def tearDown(self) -> None:
        self.university_model = None
        self.controller = None

    def testExecute_return400_whenInvalidUniversityID(self):
        # Arrange

        # Act
        result = self.controller.execute({'university_id': 'invalid uuid'})

        # Assert
        self.university_model.get_university_courses.assert_not_called()
        self.assertEqual(400, result.status_code)

    def testExecute_return404_whenUniversityDontExist(self):
        # Arrange
        self.university_model.get_university_by_id.return_value = None

        # Act
        result = self.controller.execute({'university_id': str(uuid.uuid4())})

        # Assert
        self.university_model.get_university_courses.assert_not_called()
        self.assertEqual(404, result.status_code)

    def testExecute_return200_whenUniversityExist(self):
        # Arrange
        first_course = Course(str(uuid.uuid4()), str(uuid.uuid4()), "Test course", "Test course description",
                              str(uuid.uuid4()), "TEST123", [Category(str(uuid.uuid4()), "Test category")])
        second_course = Course(str(uuid.uuid4()), first_course.university_id, "name", "description", str(uuid.uuid4()),
                               "code", [])
        expected_result = [first_course.dump(), second_course.dump()]
        self.university_model.get_university_by_id.return_value = University(str(uuid.uuid4()), 'Name')
        self.university_model.get_university_courses.return_value = [first_course, second_course]

        # Act
        result = self.controller.execute({'university_id': str(uuid.uuid4())})

        # Assert
        self.university_model.get_university_courses.assert_called_once()
        self.assertEqual(200, result.status_code)
        self.assertEqual(expected_result, json.loads(result.data))
