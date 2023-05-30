import unittest
from unittest.mock import MagicMock
from app.stuquiz.repositories.university_repository import UniversityRepository
from app.stuquiz.entities.university import University


class UniversityRepositoryTest(unittest.TestCase):

    def test_insert(self):
        # Create a mock University object
        university = University(name="Test University", uuid=None, id=None)

        # Create a mock database connection and cursor
        mock_db = MagicMock()
        mock_cursor = MagicMock()
        mock_db.cursor.return_value = mock_cursor

        # Mock the execute and commit methods
        mock_cursor.execute.return_value = None
        mock_db.commit.return_value = None

        # Create an instance of the repository and set the mock database connection
        repository = UniversityRepository()
        repository.db = mock_db

        # Call the insert method
        result = repository.insert(university)

        # Assert that the execute method was called with the correct query and values
        mock_cursor.execute.assert_called_once_with(
            "INSERT INTO university (name) VALUES (%s)",
            (university.name,)
        )

        # Assert that the commit method was called
        mock_db.commit.assert_called_once()

        # Assert that the result is True (insertion successful)
        self.assertTrue(result)

    # Implement similar test methods for other repository methods (delete, update, select_by_id)

    if __name__ == '__main__':
        unittest.main()