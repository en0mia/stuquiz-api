# @author Lorenzo Varese
# @created 2023-06-30

import unittest
import uuid
from datetime import datetime
from unittest.mock import MagicMock

from app.stuquiz.entities.question import Question
from app.stuquiz.repositories.question_repository import QuestionRepository


class TestQuestionRepository(unittest.TestCase):
    test_question = None
    NON_EXISTING_ID = 'test-id'

    def setUp(self) -> None:
        self.cursor = MagicMock()
        self.db = MagicMock()
        self.db_provider = MagicMock()

        self.db.cursor.return_value = self.cursor
        self.db_provider.get_db.return_value = self.db
        self.repository = QuestionRepository(self.db_provider)

        self.test_question = Question(
            id=str(uuid.uuid4()),
            course_id=str(uuid.uuid4()),
            question="Test question",
            creation_date=datetime.now(),
            rating=5
        )

    def tearDown(self) -> None:
        self.cursor = None
        self.db = None
        self.db_provider = None
        self.repository = None
        self.test_question = None

    def test_create_question(self):
        # Arrange
        expected_query = 'INSERT INTO question (question, rating, course_id) VALUES (%s, %s, %s)'
        expected_args = (self.test_question.question, self.test_question.rating, self.test_question.course_id)

        # Act
        result = self.repository.create_question(self.test_question)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_args)

        self.db.commit.assert_called_once()

        self.assertTrue(result)

    def test_delete_question(self):
        # Arrange
        expected_query = 'DELETE FROM question WHERE id = %s'
        expected_arg = (self.test_question.id, )

        # Act
        result = self.repository.delete_question(self.test_question)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_arg)

        self.db.commit.assert_called_once()

        self.assertTrue(result)

    def test_update_question_text(self):
        # Arrange
        expected_query = 'UPDATE question SET question = %s WHERE id = %s'
        expected_args = (self.test_question.question, self.test_question.id)

        # Act
        result = self.repository.update_question_text(self.test_question)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_args)

        self.db.commit.assert_called_once()

        self.assertTrue(result)

    def test_select_question_by_id_when_question_exists(self):
        # Arrange
        expected_result = Question(self.test_question.id, self.test_question.course_id,
                                   self.test_question.question, self.test_question.creation_date,
                                   self.test_question.rating)
        self.cursor.fetchall.return_value = [(self.test_question.id, self.test_question.course_id,
                                              self.test_question.question, self.test_question.creation_date,
                                              self.test_question.rating)]
        expected_query = 'SELECT id, course_id, question, creation_date, rating FROM question WHERE id = %s'
        expected_arg = (self.test_question.id, )

        # Act
        result = self.repository.select_question_by_id(self.test_question.id)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_arg)
        self.assertEqual(expected_result, result)

    def test_select_question_by_id_when_question_doesnt_exist(self):
        # Arrange
        self.cursor.fetchall.return_value = None
        expected_query = 'SELECT id, course_id, question, creation_date, rating FROM question WHERE id = %s'
        expected_arg = (self.NON_EXISTING_ID, )

        # Act
        result = self.repository.select_question_by_id(self.NON_EXISTING_ID)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_arg)
        self.assertIsNone(result)
