# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 05/07/23
import hashlib
import unittest
import uuid
from unittest.mock import MagicMock

from app.stuquiz.entities.admin import Admin
from app.stuquiz.repositories.admin_repository import AdminRepository


class TestAdminRepository(unittest.TestCase):
    TEST_PASSWORD = 'password'
    TEST_SALT = 'salt'
    TEST_HASHED_PASSWORD = hashlib.pbkdf2_hmac(
        'sha256', TEST_PASSWORD.encode('utf-8'),
        TEST_SALT.encode('utf-8'), 100000
    ).hex()
    TEST_ADMIN = Admin(str(uuid.uuid4()), 'username', 'test@test.com', TEST_HASHED_PASSWORD, TEST_SALT)

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
        expected_arg = (self.TEST_ADMIN.id, )
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
        expected_arg = (self.TEST_ADMIN.id, )
        self.cursor.fetchall.return_value = []

        # Act
        result = self.repository.select_admin_by_id(self.TEST_ADMIN.id)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_arg)
        self.assertIsNone(result)

    def testSelectAdminByEmail_returnAdmin_whenAdminExist(self):
        # Arrange
        expected_query = 'SELECT id, username, email, password, salt FROM admin WHERE email = %s'
        expected_arg = (self.TEST_ADMIN.email, )
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
        expected_arg = (self.TEST_ADMIN.email, )
        self.cursor.fetchall.return_value = []

        # Act
        result = self.repository.select_admin_by_email(self.TEST_ADMIN.email)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_arg)
        self.assertIsNone(result)

    def testSelectAdminByEmailPassword_returnAdmin_whenAdminExist(self):
        # Arrange
        expected_query = 'SELECT id, username, email, password, salt FROM admin WHERE email = %s AND password = %s'
        expected_arg = (self.TEST_ADMIN.email, self.TEST_HASHED_PASSWORD)
        self.cursor.fetchall.return_value = [(
            self.TEST_ADMIN.id,
            self.TEST_ADMIN.username,
            self.TEST_ADMIN.email,
            self.TEST_ADMIN.password,
            self.TEST_ADMIN.salt
        )]

        # Act
        result = self.repository.select_admin_by_email_password(self.TEST_ADMIN.email, self.TEST_HASHED_PASSWORD)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_arg)
        self.assertEqual(self.TEST_ADMIN, result)

    def testSelectAdminByEmailPassword_returnNone_whenAdminDontExist(self):
        # Arrange
        expected_query = 'SELECT id, username, email, password, salt FROM admin WHERE email = %s AND password = %s'
        expected_arg = (self.TEST_ADMIN.email, self.TEST_ADMIN.password)
        self.cursor.fetchall.return_value = []

        # Act
        result = self.repository.select_admin_by_email_password(self.TEST_ADMIN.email, self.TEST_HASHED_PASSWORD)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_arg)
        self.assertIsNone(result)
