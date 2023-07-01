# @author Lorenzo Varese
# @created 2023-06-30

import unittest
import uuid
from unittest.mock import MagicMock

from app.stuquiz.entities.answer import Answer
from app.stuquiz.repositories.answer_repository import AnswerRepository
from app.tests.repositories.test_constants import TEST_ANSWER


class TestAnswerRepository(unittest.TestCase):
    TEST_ID = TEST_ANSWER.id
    test_answer = TEST_ANSWER

    def setUp(self) -> None:
        self.cursor = MagicMock()
        self.db = MagicMock()
        self.db_provider = MagicMock()

        self.db.cursor.return_value = self.cursor
        self.db_provider.get_db.return_value = self.db
        self.repository = AnswerRepository(self.db_provider)

    def tearDown(self) -> None:
        self.cursor = None
        self.db = None
        self.db_provider = None
        self.repository = None

    def test_create_answer(self):
        answer = Answer(
            id=self.TEST_ID,
            question_id='question_id_1',
            answer='Sample answer',
            creation_date='2023-06-30',
            correct=True,
            points=10
        )

        # Call the create_answer method
        result = self.repository.create_answer(answer)

        # Assert that the insert method was called with the correct query and arguments
        expected_query = 'INSERT INTO answer(question_id, answer, creation_date, correct, points) ' \
                         'VALUES (%s, %s, %s, %s, %s);'
        expected_args = (answer.question_id, answer.answer, answer.creation_date, answer.correct,
                         answer.points)
        self.cursor.execute.assert_called_once_with(expected_query, expected_args)

        # Assert that the commit method was called on the database connection
        self.db.commit.assert_called_once()

        # Assert that the result is True, indicating successful insertion
        self.assertTrue(result)

    def test_delete_answer(self):
        answer = Answer(
            id=self.TEST_ID,
            question_id='question_id_1',
            answer='Sample answer',
            creation_date='2023-06-30',
            correct=True,
            points=10
        )

        # Call the delete_answer method
        result = self.repository.delete_answer(answer)

        # Assert that the delete method was called with the correct query and argument
        expected_query = 'DELETE FROM answer WHERE id = %s'
        expected_arg = answer.id
        self.cursor.execute.assert_called_once_with(expected_query, expected_arg)

        # Assert that the commit method was called on the database connection
        self.db.commit.assert_called_once()

        # Assert that the result is True, indicating successful deletion
        self.assertTrue(result)

    def test_update_answer_text(self):
        answer = Answer(
            id=self.TEST_ID,
            question_id='question_id_1',
            answer='Sample answer',
            creation_date='2023-06-30',
            correct=True,
            points=10
        )

        # Call the update_answer_text method
        result = self.repository.update_answer_text(answer)

        # Assert that the update method was called with the correct query and arguments
        expected_query = 'UPDATE answer SET answer = %s WHERE id = %s'
        expected_args = (answer.answer, answer.id)
        self.cursor.execute.assert_called_once_with(expected_query, expected_args)

        # Assert that the commit method was called on the database connection
        self.db.commit.assert_called_once()

        # Assert that the result is True, indicating successful update
        self.assertTrue(result)

    def test_select_answer_by_id_when_answer_exists(self):
        # Arrange
        expected_result = Answer(self.test_answer.id, self.test_answer.question_id,
                                 self.test_answer.answer, self.test_answer.creation_date,
                                 self.test_answer.correct, self.test_answer.points)

        self.cursor.fetchall.return_value = [(self.test_answer.id, self.test_answer.question_id,
                                              self.test_answer.answer, self.test_answer.creation_date,
                                              self.test_answer.correct, self.test_answer.points)]

        # Act
        result = self.repository.select_answer_by_id(self.test_answer.id)

        # Assert
        self.assertEqual(expected_result, result)

    def test_select_answer_by_id_when_answer_doesnt_exist(self):
        # Arrange
        self.cursor.fetchall.return_value = None

        # Act
        result = self.repository.select_answer_by_id(self.TEST_ID)

        # Assert
        self.assertIsNone(result)
