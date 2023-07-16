# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 04/07/23
import unittest
import uuid
from unittest.mock import MagicMock

from app.stuquiz.entities.university import University
from app.stuquiz.models.university.university_model import UniversityModel


class TestUniversityModel(unittest.TestCase):
    TEST_UNIVERSITY = University(str(uuid.uuid4()), 'University Name')

    def setUp(self) -> None:
        self.university_repository = MagicMock()
        self.course_repository = MagicMock()
        self.model = UniversityModel(self.university_repository, self.course_repository)

    def tearDown(self) -> None:
        self.university_repository = None
        self.course_repository = None
        self.model = None

    def testGetUniversities_callRepository_whenCalled(self):
        # Arrange
        self.university_repository.select_universities.return_value = []

        # Act
        self.model.get_universities()

        # Assert
        self.university_repository.select_universities.assert_called_once()

    def testGetUniversityById_callRepository_whenCalled(self):
        # Arrange
        self.university_repository.select_university_by_id.return_value = []

        # Act
        self.model.get_university_by_id('')

        # Assert
        self.university_repository.select_university_by_id.assert_called_once()

    def testUpdateUniversity_callRepository_whenCalled(self):
        # Arrange

        # Act
        self.model.update_university(self.TEST_UNIVERSITY)

        # Assert
        self.university_repository.update_university.assert_called_once()

    def testDeleteUniversity_callRepository_whenCalled(self):
        # Arrange

        # Act
        self.model.delete_university(self.TEST_UNIVERSITY)

        # Assert
        self.university_repository.delete_university.assert_called_once()

    def testGetUniversityCourses_callRepository_whenCalled(self):
        # Arrange

        # Act
        self.model.get_university_courses(self.TEST_UNIVERSITY)

        # Assert
        self.course_repository.select_courses_by_university_id.assert_called_once()
