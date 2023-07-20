# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 18/07/23
import unittest
import uuid
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

    def testGetCourseById_callRepository_whenCalled(self):
        # Arrange
        self.course_repository.get_course_by_id.return_value = []

        # Act
        self.model.get_course_by_id(str(uuid.uuid4()))

        # Assert
        self.course_repository.select_course_by_id.assert_called_once()

    def testGetCoursesByProfessor_callRepository_whenCalled(self):
        # Arrange
        self.course_repository.select_courses_by_professor_id.return_value = []

        # Act
        self.model.get_courses_by_professor(str(uuid.uuid4()))

        # Assert
        self.course_repository.select_courses_by_professor_id.assert_called_once()

    def testGetCoursesByCategory_callRepository_whenCalled(self):
        # Arrange
        self.course_repository.select_courses_by_category_id.return_value = []

        # Act
        self.model.get_courses_by_category(str(uuid.uuid4()))

        # Assert
        self.course_repository.select_courses_by_category_id.assert_called_once()

    def testAddCourse_callRepository_whenCalled(self):
        # Arrange
        self.course_repository.create_course.return_value = True

        # Act
        self.model.add_course(str(uuid.uuid4()), 'name', 'description', str(uuid.uuid4()), 'code')

        # Assert
        self.course_repository.create_course.assert_called_once()

    def testUpdateCourse_callRepository_whenCalled(self):
        # Arrange
        self.course_repository.update_course.return_value = True

        # Act
        self.model.update_course(str(uuid.uuid4()), str(uuid.uuid4()), 'name', 'description', str(uuid.uuid4()), 'code')

        # Assert
        self.course_repository.update_course.assert_called_once()
