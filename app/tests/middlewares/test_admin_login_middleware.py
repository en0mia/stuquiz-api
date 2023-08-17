# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 24/07/23
import unittest
from unittest.mock import MagicMock

from app.stuquiz.middlewares.admin_login_middleware import AdminLoginMiddleware


class TestAdminLoginMiddleware(unittest.TestCase):
    def setUp(self) -> None:
        self.admin_model = MagicMock()
        self.request = MagicMock()
        self.middleware = AdminLoginMiddleware(self.admin_model)

    def tearDown(self) -> None:
        self.admin_model = None
        self.request = None
        self.middleware = None

    def testDispatch_return401_whenAdminNotLoggedIn(self):
        # Arrange
        self.admin_model.is_admin_logged_in.return_value = False

        # Act
        result = self.middleware.dispatch(self.request)

        # Assert
        self.admin_model.is_admin_logged_in.assert_called_once()
        self.assertEqual(401, result.status_code)

    def testDispatch_returnNone_whenAdminLoggedIn(self):
        # Arrange
        self.admin_model.is_admin_logged_in.return_value = True

        # Act
        result = self.middleware.dispatch(self.request)

        # Assert
        self.admin_model.is_admin_logged_in.assert_called_once()
        self.assertIsNone(result)
