# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 18/07/23
import json
import unittest
import uuid
from unittest.mock import MagicMock

from app.stuquiz.controllers.course.get_course_by_id_controller import GetCourseByIdController
from app.stuquiz.entities.category import Category
from app.stuquiz.entities.course import Course


class TestGetCourseByIdController(unittest.TestCase):
    TEST_CATEGORY = Category(str(uuid.uuid4()), "Test category")
    TEST_COURSE = Course(str(uuid.uuid4()), str(uuid.uuid4()), "Test course", "Test course description",
                         "Test professor", "TEST123", [TEST_CATEGORY])

    def setUp(self) -> None:
        self.course_model = MagicMock()
        self.controller = GetCourseByIdController(self.course_model)

    def tearDown(self) -> None:
        self.course_model = None
        self.controller = None

    def testExecute_return400_whenInvalidCourseId(self):
        # Arrange
        self.course_model.get_course_by_id.return_value = None

        # Act
        result = self.controller.execute({'course_id': 'invalid id'})

        # Assert
        self.course_model.get_course_by_id.assert_not_called()
        self.assertEqual(400, result.status_code)

    def testExecute_return404_whenCourseDontExist(self):
        # Arrange
        self.course_model.get_course_by_id.return_value = None

        # Act
        result = self.controller.execute({'course_id': self.TEST_COURSE.id})

        # Assert
        self.course_model.get_course_by_id.assert_called_once()
        self.assertEqual(404, result.status_code)

    def testExecute_return200_whenCourseExist(self):
        # Arrange
        expected_body = {
            'id': self.TEST_COURSE.id,
            'university_id': self.TEST_COURSE.university_id,
            'name': self.TEST_COURSE.name,
            'description': self.TEST_COURSE.description,
            'professor': self.TEST_COURSE.professor,
            'categories': [category.dump() for category in self.TEST_COURSE.categories],
            'code': self.TEST_COURSE.code
        }
        self.course_model.get_course_by_id.return_value = self.TEST_COURSE

        # Act
        result = self.controller.execute({'course_id': self.TEST_COURSE.id})

        # Assert
        self.course_model.get_course_by_id.assert_called_once()
        self.assertEqual(200, result.status_code)
        self.assertEqual(expected_body, json.loads(result.data))
