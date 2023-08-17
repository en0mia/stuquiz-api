# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 19/07/23
import json
import unittest
import uuid
from unittest import mock
from unittest.mock import MagicMock

from app.stuquiz.controllers.course.get_courses_by_category_controller import GetCoursesByCategoryController
from app.tests.controllers.course.course_controllers_utils import CourseControllersUtils


class TestGetCoursesByCategoryController(unittest.TestCase):
    def setUp(self) -> None:
        self.request = MagicMock()
        self.course_model = MagicMock()
        self.controller = GetCoursesByCategoryController(self.course_model)
        self.args = mock.PropertyMock(return_value={'category_id': str(uuid.uuid4())})
        type(self.request).args = self.args

    def tearDown(self) -> None:
        self.request = None
        self.course_model = None
        self.controller = None
        self.args = None

    def testExecute_return200_whenCoursesExist(self):
        # Arrange
        courses = CourseControllersUtils.generate_courses(2)
        expected_body = CourseControllersUtils.generate_expected_body(courses)
        self.course_model.get_courses_by_category.return_value = courses

        # Act
        result = self.controller.execute(self.request)

        # Assert
        self.args.assert_called_once()
        self.course_model.get_courses_by_category.assert_called_once()
        self.assertEqual(200, result.status_code)
        self.assertEqual(expected_body, json.loads(result.data))

    def testExecute_return200WithEmptyBody_whenCoursesDontExist(self):
        # Arrange
        expected_body = []
        self.course_model.get_courses_by_category.return_value = []

        # Act
        result = self.controller.execute(self.request)

        # Assert
        self.args.assert_called_once()
        self.course_model.get_courses_by_category.assert_called_once()
        self.assertEqual(200, result.status_code)
        self.assertEqual(expected_body, json.loads(result.data))
