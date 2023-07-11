# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 05/07/23
import hashlib
import unittest
import uuid
from unittest.mock import MagicMock

from app.stuquiz.entities.admin import Admin
from app.stuquiz.models.admin.admin_model import AdminModel


class TestAdminModel(unittest.TestCase):
    TEST_PASSWORD = 'password'
    TEST_SALT = 'salt'
    HASHED_PASSWORD = hashlib.pbkdf2_hmac('sha256', TEST_PASSWORD.encode('utf-8'), TEST_SALT.encode('utf-8'),
                                          100000).hex()
    TEST_ADMIN = Admin(str(uuid.uuid4()), 'username', 'test@test.com', HASHED_PASSWORD, TEST_SALT)

    def setUp(self) -> None:
        self.admin_repository = MagicMock()
        self.admin_model = AdminModel(self.admin_repository)

    def tearDown(self) -> None:
        self.admin_repository = None
        self.admin_model = None

    def testGetAdminById_returnNone_whenAdminDontExist(self):
        # Arrange
        self.admin_repository.select_admin_by_id.return_value = None

        # Act
        result = self.admin_model.get_admin_by_id(self.TEST_ADMIN.id)

        # Assert
        self.assertIsNone(result)

    def testGetAdminById_returnAdmin_whenAdminExist(self):
        # Arrange
        self.admin_repository.select_admin_by_id.return_value = self.TEST_ADMIN

        # Act
        result = self.admin_model.get_admin_by_id(self.TEST_ADMIN.id)

        # Assert
        self.admin_repository.select_admin_by_id.assert_called_once()
        self.assertEqual(self.TEST_ADMIN, result)

    def testLoginAdmin_returnNone_whenAdminDontExist(self):
        # Arrange
        self.admin_repository.select_admin_by_email.return_value = None

        # Act
        result = self.admin_model.login_admin(self.TEST_ADMIN.email, self.TEST_ADMIN.password)

        # Assert
        self.admin_repository.select_admin_by_email.assert_called_once()
        self.assertIsNone(result)

    def testLoginAdmin_returnNone_whenIncorrectPassword(self):
        # Arrange
        self.admin_repository.select_admin_by_email.return_value = self.TEST_ADMIN
        self.admin_repository.select_admin_by_email_password.return_value = None

        # Act
        result = self.admin_model.login_admin(self.TEST_ADMIN.email, 'wrong password')

        # Assert
        self.admin_repository.select_admin_by_email.assert_called_once()
        self.assertIsNone(result)

    def testLoginAdmin_returnAdminId_whenCorrectPassword(self):
        # Arrange
        self.admin_repository.select_admin_by_email.return_value = self.TEST_ADMIN
        self.admin_repository.select_admin_by_email_password.return_value = self.TEST_ADMIN

        # Act
        result = self.admin_model.login_admin(self.TEST_ADMIN.email, self.TEST_PASSWORD)

        # Assert
        self.admin_repository.select_admin_by_email.assert_called_once()
        self.assertEqual(self.TEST_ADMIN.id, result)
