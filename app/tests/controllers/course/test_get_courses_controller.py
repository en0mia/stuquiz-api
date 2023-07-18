# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 18/07/23
import json
import unittest
import uuid
from unittest.mock import MagicMock

from app.stuquiz.controllers.course.get_courses_controller import GetCoursesController
from app.stuquiz.entities.category import Category
from app.stuquiz.entities.course import Course


class TestGetCoursesController(unittest.TestCase):
    TEST_CATEGORY = Category(str(uuid.uuid4()), "Test category")
    TEST_COURSE = Course(str(uuid.uuid4()), str(uuid.uuid4()), "Test course", "Test course description",
                         "Test professor", "TEST123", [TEST_CATEGORY])

    def setUp(self) -> None:
        self.course_model = MagicMock()
        self.controller = GetCoursesController(self.course_model)

    def tearDown(self) -> None:
        self.course_model = None
        self.controller = None

    def testExecute_return200WithEmptyBody_whenCoursesDontExist(self):
        # Arrange
        expected_body = []
        self.course_model.get_courses.return_value = []

        # Act
        result = self.controller.execute({})

        # Assert
        self.course_model.get_courses.assert_called_once()
        self.assertEqual(200, result.status_code)
        self.assertEqual(expected_body, json.loads(result.data))

    def testExecute_return200_whenCoursesExist(self):
        # Arrange
        first_course = Course(str(uuid.uuid4()), str(uuid.uuid4()), "Test course 1", "Test course 1 description",
                              "Test professor 1", "TEST1", [self.TEST_CATEGORY])
        second_course = Course(str(uuid.uuid4()), str(uuid.uuid4()), "Test course 2", "Test course 2 description",
                               "Test professor 2", "TEST2", [])
        expected_body = [
            {
                'id': first_course.id,
                'university_id': first_course.university_id,
                'name': first_course.name,
                'description': first_course.description,
                'professor': first_course.professor,
                'categories': [category.dump() for category in first_course.categories],
                'code': first_course.code
            },
            {
                'id': second_course.id,
                'university_id': second_course.university_id,
                'name': second_course.name,
                'description': second_course.description,
                'professor': second_course.professor,
                'categories': [category.dump() for category in second_course.categories],
                'code': second_course.code
            }
        ]
        self.course_model.get_courses.return_value = [first_course, second_course]

        # Act
        result = self.controller.execute({})

        # Assert
        self.course_model.get_courses.assert_called_once()
        self.assertEqual(200, result.status_code)
        self.assertEqual(expected_body, json.loads(result.data))
