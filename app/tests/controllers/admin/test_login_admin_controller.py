# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 05/07/23
import unittest
import uuid
from unittest import mock
from unittest.mock import MagicMock

from app.stuquiz.controllers.admin.login_admin_controller import LoginAdminController
from app.stuquiz.entities.admin import Admin


class TestLoginAdminController(unittest.TestCase):
    TEST_VALID_EMAIL = 'test@test.com'
    TEST_INVALID_EMAIL = 'Not a valid email'
    TEST_PASSWORD = 'password'
    TEST_ADMIN = Admin(str(uuid.uuid4()), 'username', TEST_VALID_EMAIL, 'password', 'salt')

    def setUp(self) -> None:
        self.request = MagicMock()
        self.admin_model = MagicMock()
        self.controller = LoginAdminController(self.admin_model)
        self.form = mock.PropertyMock(return_value={'email': self.TEST_VALID_EMAIL, 'password': self.TEST_PASSWORD})
        type(self.request).form = self.form

    def tearDown(self) -> None:
        self.request = None
        self.admin_model = None
        self.controller = None
        self.form = None

    def testExecute_return401_whenAdminDontExist(self):
        # Arrange
        self.admin_model.login_admin.return_value = None

        # Act
        result = self.controller.execute(self.request)

        # Assert
        self.assertEqual(2, self.form.call_count)
        self.admin_model.login_admin.assert_called_once()
        self.assertEqual(401, result.status_code)

    def testExecute_return200_whenLoginSuccessful(self):
        # Arrange
        self.admin_model.login_admin.return_value = self.TEST_ADMIN

        # Act
        result = self.controller.execute(self.request)

        # Assert
        self.assertEqual(2, self.form.call_count)
        self.admin_model.login_admin.assert_called_once()
        self.admin_model.store_session.assert_called_once()
        self.assertEqual(200, result.status_code)
