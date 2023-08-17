# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 20/07/23
import json
import unittest
import uuid
from unittest import mock
from unittest.mock import MagicMock

from app.stuquiz.controllers.course.delete_course_controller import DeleteCourseController
from app.tests.controllers.course.course_controllers_utils import CourseControllersUtils


class TestDeleteCourseController(unittest.TestCase):
    def setUp(self) -> None:
        self.request = MagicMock()
        self.course_model = MagicMock()
        self.admin_model = MagicMock()
        self.controller = DeleteCourseController(self.course_model)
        self.args = mock.PropertyMock(return_value={'course_id': str(uuid.uuid4())})
        type(self.request).args = self.args

    def tearDown(self) -> None:
        self.request = None
        self.course_model = None
        self.admin_model = None
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
        self.course_model.delete_course.assert_not_called()
        self.assertEqual(404, result.status_code)

    def testExecute_return500_whenDbError(self):
        # Arrange
        course = CourseControllersUtils.generate_courses(1)
        self.course_model.delete_course.return_value = False
        self.course_model.get_course_by_id.return_value = course[0]

        # Act
        result = self.controller.execute(self.request)

        # Assert
        self.args.assert_called_once()
        self.course_model.delete_course.assert_called_once()
        self.assertEqual(500, result.status_code)

    def testExecute_return200WithEmptyBody_whenCourseHasBeenDeleted(self):
        # Arrange
        expected_body = {}
        self.course_model.delete_course.return_value = True

        # Act
        result = self.controller.execute(self.request)

        # Assert
        self.args.assert_called_once()
        self.course_model.delete_course.assert_called_once()
        self.assertEqual(200, result.status_code)
        self.assertEqual(expected_body, json.loads(result.data))
