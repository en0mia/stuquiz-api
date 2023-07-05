# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 05/07/23
import unittest
import uuid
from unittest.mock import MagicMock

from app.stuquiz.entities.admin import Admin
from app.stuquiz.repositories.admin_repository import AdminRepository


class TestAdminRepository(unittest.TestCase):
    TEST_ADMIN = Admin(str(uuid.uuid4()), 'username', 'test@test.com', 'password', 'salt')

    def setUp(self) -> None:
        self.cursor = MagicMock()
        self.db = MagicMock()
        self.db_provider = MagicMock()

        self.db.cursor.return_value = self.cursor
        self.db_provider.get_db.return_value = self.db
        self.repository = AdminRepository(self.db_provider)

    def tearDown(self) -> None:
        self.cursor = None
        self.db = None
        self.db_provider = None
        self.repository = None

    def testSelectAdminById_returnAdmin_whenAdminExist(self):
        # Arrange
        expected_query = 'SELECT id, username, email, password, salt FROM admin WHERE id = %s'
        expected_arg = self.TEST_ADMIN.id
        self.cursor.fetchall.return_value = [(
            self.TEST_ADMIN.id,
            self.TEST_ADMIN.username,
            self.TEST_ADMIN.email,
            self.TEST_ADMIN.password,
            self.TEST_ADMIN.salt
        )]

        # Act
        result = self.repository.select_admin_by_id(self.TEST_ADMIN.id)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_arg)
        self.assertEqual(self.TEST_ADMIN, result)

    def testSelectAdminById_returnNone_whenAdminDontExist(self):
        # Arrange
        expected_query = 'SELECT id, username, email, password, salt FROM admin WHERE id = %s'
        expected_arg = self.TEST_ADMIN.id
        self.cursor.fetchall.return_value = []

        # Act
        result = self.repository.select_admin_by_id(self.TEST_ADMIN.id)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_arg)
        self.assertIsNone(result)

    def testSelectAdminByEmail_returnAdmin_whenAdminExist(self):
        # Arrange
        expected_query = 'SELECT id, username, email, password, salt FROM admin WHERE email = %s'
        expected_arg = self.TEST_ADMIN.email
        self.cursor.fetchall.return_value = [(
            self.TEST_ADMIN.id,
            self.TEST_ADMIN.username,
            self.TEST_ADMIN.email,
            self.TEST_ADMIN.password,
            self.TEST_ADMIN.salt
        )]

        # Act
        result = self.repository.select_admin_by_email(self.TEST_ADMIN.email)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_arg)
        self.assertEqual(self.TEST_ADMIN, result)

    def testSelectAdminByEmail_returnNone_whenAdminDontExist(self):
        # Arrange
        expected_query = 'SELECT id, username, email, password, salt FROM admin WHERE email = %s'
        expected_arg = self.TEST_ADMIN.email
        self.cursor.fetchall.return_value = []

        # Act
        result = self.repository.select_admin_by_email(self.TEST_ADMIN.email)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_arg)
        self.assertIsNone(result)
