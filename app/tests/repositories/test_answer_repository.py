# @author Lorenzo Varese
# @created 2023-06-30

import unittest
import uuid
from datetime import datetime
from unittest.mock import MagicMock

from app.stuquiz.entities.answer import Answer
from app.stuquiz.repositories.answer_repository import AnswerRepository


class TestAnswerRepository(unittest.TestCase):
    TEST_ANSWER = Answer(str(uuid.uuid4()), str(uuid.uuid4()), "Test answer", datetime.now(), True, 10.0)

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

    def testCreateAnswer_ReturnTrue_WhenAnswerCreated(self):
        # Arrange
        expected_query = 'INSERT INTO answer(question_id, answer, creation_date, correct, points) ' \
                         'VALUES (%s, %s, %s, %s, %s);'
        expected_args = (self.TEST_ANSWER.question_id, self.TEST_ANSWER.answer, self.TEST_ANSWER.creation_date,
                         self.TEST_ANSWER.correct, self.TEST_ANSWER.points)

        # Act
        result = self.repository.create_answer(self.TEST_ANSWER)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_args)
        self.db.commit.assert_called_once()
        self.assertTrue(result)

    def testDeleteAnswer_ReturnTrue_WhenAnswerDeleted(self):
        # Arrange
        expected_query = 'DELETE FROM answer WHERE id = %s'
        expected_arg = (self.TEST_ANSWER.id, )

        # Act
        result = self.repository.delete_answer(self.TEST_ANSWER)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_arg)
        self.db.commit.assert_called_once()
        self.assertTrue(result)

    def testUpdateAnswer_ReturnTrue_WhenAnswerUpdated(self):
        # Arrange
        expected_query = 'UPDATE answer SET answer = %s WHERE id = %s'
        expected_args = (self.TEST_ANSWER.answer, self.TEST_ANSWER.id)

        # Act
        result = self.repository.update_answer_text(self.TEST_ANSWER)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_args)

        self.db.commit.assert_called_once()

        self.assertTrue(result)

    def testSelectAnswerById_ReturnAnswer_WhenAnswerExist(self):
        # Arrange
        expected_result = Answer(self.TEST_ANSWER.id, self.TEST_ANSWER.question_id,
                                 self.TEST_ANSWER.answer, self.TEST_ANSWER.creation_date,
                                 self.TEST_ANSWER.correct, self.TEST_ANSWER.points)
        self.cursor.fetchall.return_value = [(self.TEST_ANSWER.id, self.TEST_ANSWER.question_id,
                                              self.TEST_ANSWER.answer, self.TEST_ANSWER.creation_date,
                                              self.TEST_ANSWER.correct, self.TEST_ANSWER.points)]

        # Act
        result = self.repository.select_answer_by_id(self.TEST_ANSWER.id)

        # Assert
        self.assertEqual(expected_result, result)

    def testSelectAnswerById_ReturnNone_WhenAnswerDontExist(self):
        # Arrange
        self.cursor.fetchall.return_value = None

        # Act
        result = self.repository.select_answer_by_id("id-00-test")

        # Assert
        self.assertIsNone(result)
