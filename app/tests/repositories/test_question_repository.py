# @author Lorenzo Varese
# @created 2023-06-30

import unittest
from datetime import datetime
from unittest.mock import MagicMock

from app.stuquiz.entities.question import Question
from app.stuquiz.repositories.question_repository import QuestionRepository
from app.tests.repositories.test_constants import TEST_QUESTION


class TestQuestionRepository(unittest.TestCase):
    TEST_ID = TEST_QUESTION.id
    test_question = TEST_QUESTION

    def setUp(self) -> None:
        self.cursor = MagicMock()
        self.db = MagicMock()
        self.db_provider = MagicMock()

        self.db.cursor.return_value = self.cursor
        self.db_provider.get_db.return_value = self.db
        self.repository = QuestionRepository(self.db_provider)

    def tearDown(self) -> None:
        self.cursor = None
        self.db = None
        self.db_provider = None
        self.repository = None

    def test_create_question(self):
        question = Question(
            id=self.TEST_ID,
            course_id='course_id_1',
            question='Sample Question',
            creation_date=datetime.now(),
            rating=5
        )

        # Call the create_question method
        result = self.repository.create_question(question)

        # Assert that the insert method was called with the correct query and arguments
        expected_query = 'INSERT INTO question (question, rating, course_id) VALUES (%s, %s, %s)'
        expected_args = (question.question, question.rating, question.course_id)
        self.cursor.execute.assert_called_once_with(expected_query, expected_args)

        # Assert that the commit method was called on the database connection
        self.db.commit.assert_called_once()

        # Assert that the result is True, indicating successful creation
        self.assertTrue(result)

    def test_delete_question(self):
        question = Question(
            id=self.TEST_ID,
            course_id='course_id_1',
            question='Sample Question',
            creation_date=datetime.now(),
            rating=5
        )

        # Call the delete_question method
        result = self.repository.delete_question(question)

        # Assert that the delete method was called with the correct query and argument
        expected_query = 'DELETE FROM question WHERE id = %s'
        expected_arg = question.id
        self.cursor.execute.assert_called_once_with(expected_query, expected_arg)

        # Assert that the commit method was called on the database connection
        self.db.commit.assert_called_once()

        # Assert that the result is True, indicating successful deletion
        self.assertTrue(result)

    def test_update_question_text(self):
        question = Question(
            id=self.TEST_ID,
            course_id='course_id_1',
            question='Sample Question',
            creation_date=datetime.now(),
            rating=5
        )

        # Call the update_question_text method
        result = self.repository.update_question_text(question)

        # Assert that the update method was called with the correct query and arguments
        expected_query = 'UPDATE question SET question = %s WHERE id = %s'
        expected_args = (question.question, question.id)
        self.cursor.execute.assert_called_once_with(expected_query, expected_args)

        # Assert that the commit method was called on the database connection
        self.db.commit.assert_called_once()

        # Assert that the result is True, indicating successful update
        self.assertTrue(result)

    def test_select_question_by_id_when_question_exists(self):
        # Arrange
        expected_result = Question(self.test_question.id, self.test_question.course_id,
                                   self.test_question.question, self.test_question.creation_date,
                                   self.test_question.rating)

        self.cursor.fetchall.return_value = [(self.test_question.id, self.test_question.course_id,
                                              self.test_question.question, self.test_question.creation_date,
                                              self.test_question.rating)]

        # Act
        result = self.repository.select_question_by_id(self.test_question.id)

        # Assert
        self.assertEqual(expected_result, result)

    def test_select_question_by_id_when_question_doesnt_exist(self):
        # Arrange
        self.cursor.fetchall.return_value = None

        # Act
        result = self.repository.select_question_by_id(self.TEST_ID)

        # Assert
        self.assertIsNone(result)
