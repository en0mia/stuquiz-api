# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 18/07/23
import json
import unittest
from unittest.mock import MagicMock

from app.stuquiz.controllers.course.get_courses_controller import GetCoursesController
from app.tests.controllers.course.course_controllers_utils import CourseControllersUtils


class TestGetCoursesController(unittest.TestCase):
    def setUp(self) -> None:
        self.request = MagicMock()
        self.course_model = MagicMock()
        self.controller = GetCoursesController(self.course_model)

    def tearDown(self) -> None:
        self.request = None
        self.course_model = None
        self.controller = None

    def testExecute_return200WithEmptyBody_whenCoursesDontExist(self):
        # Arrange
        expected_body = []
        self.course_model.get_courses.return_value = []

        # Act
        result = self.controller.execute(self.request)

        # Assert
        self.course_model.get_courses.assert_called_once()
        self.assertEqual(200, result.status_code)
        self.assertEqual(expected_body, json.loads(result.data))

    def testExecute_return200_whenCoursesExist(self):
        # Arrange
        courses = CourseControllersUtils.generate_courses(2)
        expected_body = CourseControllersUtils.generate_expected_body(courses)
        self.course_model.get_courses.return_value = courses

        # Act
        result = self.controller.execute(self.request)

        # Assert
        self.course_model.get_courses.assert_called_once()
        self.assertEqual(200, result.status_code)
        self.assertEqual(expected_body, json.loads(result.data))
