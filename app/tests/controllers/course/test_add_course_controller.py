# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 19/07/23
import json
import unittest
import uuid
from unittest import mock
from unittest.mock import MagicMock

from app.stuquiz.controllers.course.add_course_controller import AddCourseController
from app.stuquiz.entities.university import University
from app.tests.controllers.course.course_controllers_utils import CourseControllersUtils


class TestAddCourseController(unittest.TestCase):
    def setUp(self) -> None:
        self.request = MagicMock()
        self.course_model = MagicMock()
        self.university_model = MagicMock()
        self.controller = AddCourseController(self.course_model, self.university_model)

    def tearDown(self) -> None:
        self.request = None
        self.course_model = None
        self.university_model = None
        self.controller = None

    def testExecute_return400_whenUniversityIdDontExist(self):
        # Arrange
        course = CourseControllersUtils.generate_courses(1)
        self.university_model.get_university_by_id.return_value = None
        form = mock.PropertyMock(return_value=course[0].dump())
        type(self.request).form = form

        # Act
        result = self.controller.execute(self.request)

        # Assert
        self.assertEqual(5, form.call_count)
        self.university_model.get_university_by_id.assert_called_once()
        self.course_model.add_course.assert_not_called()
        self.assertEqual(400, result.status_code)

    def testExecute_return500_whenDbError(self):
        # Arrange
        course = CourseControllersUtils.generate_courses(1)
        self.course_model.add_course.return_value = False
        self.university_model.get_university_by_id.return_value = University(str(uuid.uuid4()), 'Name')
        form = mock.PropertyMock(return_value=course[0].dump())
        type(self.request).form = form

        # Act
        result = self.controller.execute(self.request)

        # Assert
        self.assertEqual(5, form.call_count)
        self.university_model.get_university_by_id.assert_called_once()
        self.course_model.add_course.assert_called_once()
        self.assertEqual(500, result.status_code)

    def testExecute_return200WithEmptyBody_whenCourseHasBeenAdded(self):
        # Arrange
        course = CourseControllersUtils.generate_courses(1)
        expected_body = {}
        self.course_model.add_course.return_value = True
        self.university_model.get_university_by_id.return_value = University(str(uuid.uuid4()), 'Name')
        form = mock.PropertyMock(return_value=course[0].dump())
        type(self.request).form = form

        # Act
        result = self.controller.execute(self.request)

        # Assert
        self.assertEqual(5, form.call_count)
        self.course_model.add_course.assert_called_once()
        self.university_model.get_university_by_id.assert_called_once()
        self.assertEqual(200, result.status_code)
        self.assertEqual(expected_body, json.loads(result.data))
