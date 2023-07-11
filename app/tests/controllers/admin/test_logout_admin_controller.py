# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 12/07/23
import json
import unittest
from unittest.mock import MagicMock

from app.stuquiz.controllers.admin.logout_admin_controller import LogoutAdminController


class TestLogoutAdminController(unittest.TestCase):

    def setUp(self) -> None:
        self.admin_model = MagicMock()
        self.controller = LogoutAdminController(self.admin_model)

    def tearDown(self) -> None:
        self.admin_model = None
        self.controller = None

    def testExecute_return401_whenNotLoggedIn(self):
        # Arrange
        self.admin_model.is_admin_logged_in.return_value = False

        # Act
        result = self.controller.execute({})

        # Assert
        self.admin_model.is_admin_logged_in.assert_called_once()
        self.admin_model.logout_admin.assert_not_called()
        self.assertEqual(401, result.status_code)

    def testExecute_return401_whenLoggedOut(self):
        # Arrange
        self.admin_model.is_admin_logged_in.return_value = True
        expected_result = {}

        # Act
        result = self.controller.execute({})

        # Assert
        self.admin_model.is_admin_logged_in.assert_called_once()
        self.admin_model.logout_admin.assert_called_once()
        self.assertEqual(200, result.status_code)
        self.assertEqual(expected_result, json.loads(result.data))
