# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 19/07/23
import unittest
from unittest.mock import MagicMock

from flask import json

from app.stuquiz.controllers.course.get_courses_by_professor_controller import GetCoursesByProfessorController
from app.tests.controllers.course.course_controllers_utils import CourseControllersUtils


class TestGetCoursesByProfessorController(unittest.TestCase):
    def setUp(self) -> None:
        self.course_model = MagicMock()
        self.controller = GetCoursesByProfessorController(self.course_model)

    def tearDown(self) -> None:
        self.course_model = None
        self.controller = None

    def testExecute_return400_whenInvalidProfessorId(self):
        # Arrange
        self.course_model.get_courses_by_professor.return_value = None

        # Act
        result = self.controller.execute({'professor_id': 'invalid id'})

        # Assert
        self.course_model.get_courses_by_professor.assert_not_called()
        self.assertEqual(400, result.status_code)

    def testExecute_return200_whenCoursesExist(self):
        # Arrange
        courses = CourseControllersUtils.generate_courses(2)
        expected_body = CourseControllersUtils.generate_expected_body(courses)
        self.course_model.get_courses_by_professor.return_value = courses

        # Act
        result = self.controller.execute({'professor_id': courses[0].professor_id})

        # Assert
        self.course_model.get_courses_by_professor.assert_called_once()
        self.assertEqual(200, result.status_code)
        self.assertEqual(expected_body, json.loads(result.data))

    def testExecute_return200WithEmptyBody_whenCoursesDontExist(self):
        # Arrange
        expected_body = []
        course = CourseControllersUtils.generate_courses(1)[0]
        self.course_model.get_courses_by_professor.return_value = []

        # Act
        result = self.controller.execute({'professor_id': course.professor_id})

        # Assert
        self.course_model.get_courses_by_professor.assert_called_once()
        self.assertEqual(200, result.status_code)
        self.assertEqual(expected_body, json.loads(result.data))
