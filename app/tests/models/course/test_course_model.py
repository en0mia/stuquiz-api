# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 18/07/23
import unittest
from unittest.mock import MagicMock

from app.stuquiz.models.course.course_model import CourseModel


class TestCourseModel(unittest.TestCase):
    def setUp(self) -> None:
        self.course_repository = MagicMock()
        self.model = CourseModel(self.course_repository)

    def tearDown(self) -> None:
        self.course_repository = None
        self.model = None

    def testGetCourses_callRepository_whenCalled(self):
        # Arrange
        self.course_repository.get_courses.return_value = []

        # Act
        self.model.get_courses()

        # Assert
        self.course_repository.select_courses.assert_called_once()
