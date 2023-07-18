# @author Lorenzo Varese
# @created 2023-06-30

import unittest
import uuid
from datetime import datetime
from unittest.mock import MagicMock

from app.stuquiz.entities.question import Question
from app.stuquiz.repositories.question_repository import QuestionRepository


class TestQuestionRepository(unittest.TestCase):
    TEST_QUESTION = Question(str(uuid.uuid4()), str(uuid.uuid4()), "Test question", datetime.now(), 5)

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

    def testCreateQuestion_ReturnTrue_WhenQuestionCreated(self):
        # Arrange
        expected_query = 'INSERT INTO question (question, rating, course_id) VALUES (%s, %s, %s)'
        expected_args = (self.TEST_QUESTION.question, self.TEST_QUESTION.rating, self.TEST_QUESTION.course_id)

        # Act
        result = self.repository.create_question(self.TEST_QUESTION)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_args)
        self.db.commit.assert_called_once()
        self.assertTrue(result)

    def testDeleteQuestion_ReturnTrue_WhenQuestionDeleted(self):
        # Arrange
        expected_query = 'DELETE FROM question WHERE id = %s'
        expected_arg = (self.TEST_QUESTION.id, )

        # Act
        result = self.repository.delete_question(self.TEST_QUESTION)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_arg)
        self.db.commit.assert_called_once()
        self.assertTrue(result)

    def testUpdateQuestion_ReturnTrue_WhenQuestionUpdated(self):
        # Arrange
        expected_query = 'UPDATE question SET question = %s WHERE id = %s'
        expected_args = (self.TEST_QUESTION.question, self.TEST_QUESTION.id)

        # Act
        result = self.repository.update_question_text(self.TEST_QUESTION)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_args)
        self.db.commit.assert_called_once()
        self.assertTrue(result)

    def testSelectQuestionById_ReturnQuestion_WhenQuestionExist(self):
        # Arrange
        expected_result = Question(self.TEST_QUESTION.id, self.TEST_QUESTION.course_id,
                                   self.TEST_QUESTION.question, self.TEST_QUESTION.creation_date,
                                   self.TEST_QUESTION.rating)

        self.cursor.fetchall.return_value = [(self.TEST_QUESTION.id, self.TEST_QUESTION.course_id,
                                              self.TEST_QUESTION.question, self.TEST_QUESTION.creation_date,
                                              self.TEST_QUESTION.rating)]

        # Act
        result = self.repository.select_question_by_id(self.TEST_QUESTION.id)

        # Assert
        self.assertEqual(expected_result, result)

    def testSelectQuestionById_ReturnNone_WhenQuestionDontExist(self):
        # Arrange
        self.cursor.fetchall.return_value = None

        # Act
        result = self.repository.select_question_by_id("test-id")

        # Assert
        self.assertIsNone(result)
