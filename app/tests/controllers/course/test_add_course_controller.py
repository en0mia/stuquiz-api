# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 19/07/23
import json
import unittest
from unittest.mock import MagicMock

from app.stuquiz.controllers.course.add_course_controller import AddCourseController
from app.tests.controllers.course.course_controllers_utils import CourseControllersUtils


class TestAddCourseController(unittest.TestCase):
    def setUp(self) -> None:
        self.course_model = MagicMock()
        self.admin_model = MagicMock()
        self.controller = AddCourseController(self.course_model, self.admin_model)

    def tearDown(self) -> None:
        self.course_model = None
        self.controller = None
        self.admin_model = None

    def testExecute_return401_whenAdminNotLoggedIn(self):
        # Arrange
        course = CourseControllersUtils.generate_courses(1)
        self.admin_model.is_admin_logged_in.return_value = False

        # Act
        result = self.controller.execute(course[0].dump())

        # Assert
        self.admin_model.is_admin_logged_in.assert_called_once()
        self.course_model.add_course.assert_not_called()
        self.assertEqual(401, result.status_code)

    def testExecute_return400_whenInvalidParameters(self):
        # Arrange
        self.admin_model.is_admin_logged_in.return_value = True

        # Act
        result = self.controller.execute({
            'university_id': 'invalid id',
            'name': None,
            'description': None,
            'professor_id': 'invalid id',
            'code': None
        })

        # Assert
        self.admin_model.is_admin_logged_in.assert_called_once()
        self.course_model.add_course.assert_not_called()
        self.assertEqual(400, result.status_code)

    def testExecute_return500_whenDbError(self):
        # Arrange
        course = CourseControllersUtils.generate_courses(1)
        self.admin_model.is_admin_logged_in.return_value = True
        self.course_model.add_course.return_value = False

        # Act
        result = self.controller.execute(course[0].dump())

        # Assert
        self.admin_model.is_admin_logged_in.assert_called_once()
        self.course_model.add_course.assert_called_once()
        self.assertEqual(500, result.status_code)

    def testExecute_return200WithEmptyBody_whenCourseHasBeenAdded(self):
        # Arrange
        course = CourseControllersUtils.generate_courses(1)
        expected_body = {}
        self.course_model.add_course.return_value = True
        self.admin_model.is_admin_logged_in.return_value = True

        # Act
        result = self.controller.execute(course[0].dump())

        # Assert
        self.admin_model.is_admin_logged_in.assert_called_once()
        self.course_model.add_course.assert_called_once()
        self.assertEqual(200, result.status_code)
        self.assertEqual(expected_body, json.loads(result.data))
