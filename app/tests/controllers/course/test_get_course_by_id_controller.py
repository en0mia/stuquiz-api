# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 18/07/23
import json
import unittest
import uuid
from unittest import mock
from unittest.mock import MagicMock

from app.stuquiz.controllers.course.get_course_by_id_controller import GetCourseByIdController
from app.tests.controllers.course.course_controllers_utils import CourseControllersUtils


class TestGetCourseByIdController(unittest.TestCase):
    def setUp(self) -> None:
        self.request = MagicMock()
        self.course_model = MagicMock()
        self.controller = GetCourseByIdController(self.course_model)
        self.args = mock.PropertyMock(return_value={'course_id': str(uuid.uuid4())})
        type(self.request).args = self.args

    def tearDown(self) -> None:
        self.request = None
        self.course_model = None
        self.controller = None
        self.args = None

    def testExecute_return404_whenCourseDontExist(self):
        # Arrange
        self.course_model.get_course_by_id.return_value = None

        # Act
        result = self.controller.execute(self.request)

        # Assert
        self.args.assert_called_once()
        self.course_model.get_course_by_id.assert_called_once()
        self.assertEqual(404, result.status_code)

    def testExecute_return200_whenCourseExist(self):
        # Arrange
        course = CourseControllersUtils.generate_courses(1)[0]
        expected_body = CourseControllersUtils.generate_expected_body([course])[0]
        self.course_model.get_course_by_id.return_value = course

        # Act
        result = self.controller.execute(self.request)

        # Assert
        self.args.assert_called_once()
        self.course_model.get_course_by_id.assert_called_once()
        self.assertEqual(200, result.status_code)
        self.assertEqual(expected_body, json.loads(result.data))
