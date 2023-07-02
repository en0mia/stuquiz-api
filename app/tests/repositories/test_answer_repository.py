# @author Lorenzo Varese
# @created 2023-06-30

import unittest
import uuid
from datetime import datetime
from unittest.mock import MagicMock

from app.stuquiz.entities.answer import Answer
from app.stuquiz.repositories.answer_repository import AnswerRepository


class TestAnswerRepository(unittest.TestCase):
    test_answer = None

    def setUp(self) -> None:
        self.cursor = MagicMock()
        self.db = MagicMock()
        self.db_provider = MagicMock()

        self.db.cursor.return_value = self.cursor
        self.db_provider.get_db.return_value = self.db
        self.repository = AnswerRepository(self.db_provider)

        self.test_answer = Answer(
            id=str(uuid.uuid4()),
            question_id=str(uuid.uuid4()),
            answer="Test answer",
            creation_date=datetime.now(),
            correct=True,
            points=10.0
        )

    def tearDown(self) -> None:
        self.cursor = None
        self.db = None
        self.db_provider = None
        self.repository = None
        self.test_answer = None

    def test_create_answer(self):
        # Arrange
        expected_query = 'INSERT INTO answer(question_id, answer, creation_date, correct, points) ' \
                         'VALUES (%s, %s, %s, %s, %s);'
        expected_args = (self.test_answer.question_id, self.test_answer.answer, self.test_answer.creation_date,
                         self.test_answer.correct, self.test_answer.points)

        # Act
        result = self.repository.create_answer(self.test_answer)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_args)

        self.db.commit.assert_called_once()

        self.assertTrue(result)

    def test_delete_answer(self):
        # Arrange
        expected_query = 'DELETE FROM answer WHERE id = %s'
        expected_arg = self.test_answer.id

        # Act
        result = self.repository.delete_answer(self.test_answer)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_arg)

        self.db.commit.assert_called_once()

        self.assertTrue(result)

    def test_update_answer_text(self):
        # Arrange
        expected_query = 'UPDATE answer SET answer = %s WHERE id = %s'
        expected_args = (self.test_answer.answer, self.test_answer.id)

        # Act
        result = self.repository.update_answer_text(self.test_answer)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_args)

        self.db.commit.assert_called_once()

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
        result = self.repository.select_answer_by_id("id-00-test")

        # Assert
        self.assertIsNone(result)
