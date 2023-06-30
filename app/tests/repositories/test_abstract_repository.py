# @author Lorenzo Varese
# @created 2023-06-30

import unittest
from unittest.mock import MagicMock, patch
from mysql.connector import DatabaseError

from app.stuquiz.repositories.abstract_repository import AbstractRepository


class TestAbstractRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.cursor = MagicMock()
        self.db = MagicMock()
        self.db_provider = MagicMock()

        self.db.cursor.return_value = self.cursor
        self.db_provider.get_db.return_value = self.db
        self.repository = AbstractRepository(self.db_provider)

    def tearDown(self) -> None:
        self.cursor = None
        self.db = None
        self.db_provider = None
        self.repository = None

    @patch.object(AbstractRepository, 'execute', MagicMock(side_effect=DatabaseError))
    def testSelect_raiseException_whenExecuteError(self):
        # Arrange

        # Act / Assert
        self.assertRaises(DatabaseError, self.repository.select, "", ("",))

    @patch.object(AbstractRepository, 'execute', MagicMock(side_effect=DatabaseError))
    def testInsert_raiseException_whenExecuteError(self):
        # Arrange

        # Act / Assert
        self.assertRaises(DatabaseError, self.repository.insert, "", ("",))

    @patch.object(AbstractRepository, 'execute', MagicMock(side_effect=DatabaseError))
    def testUpdate_raiseException_whenExecuteError(self):
        # Arrange

        # Act / Assert
        self.assertRaises(DatabaseError, self.repository.update, "", ("",))

    @patch.object(AbstractRepository, 'execute', MagicMock(side_effect=DatabaseError))
    def testDelete_raiseException_whenExecuteError(self):
        # Arrange

        # Act / Assert
        self.assertRaises(DatabaseError, self.repository.delete, "", ("",))
