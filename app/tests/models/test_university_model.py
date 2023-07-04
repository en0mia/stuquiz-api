# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 04/07/23
import unittest
from unittest.mock import MagicMock

from app.stuquiz.models.university.university_model import UniversityModel


class TestUniversityModel(unittest.TestCase):
    def setUp(self) -> None:
        self.university_repository = MagicMock()
        self.model = UniversityModel(self.university_repository)

    def tearDown(self) -> None:
        self.university_repository = None
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
