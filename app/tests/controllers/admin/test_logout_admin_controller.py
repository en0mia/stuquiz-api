# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 12/07/23
import json
import unittest
from unittest.mock import MagicMock

from app.stuquiz.controllers.admin.logout_admin_controller import LogoutAdminController


class TestLogoutAdminController(unittest.TestCase):

    def setUp(self) -> None:
        self.request = MagicMock()
        self.admin_model = MagicMock()
        self.controller = LogoutAdminController(self.admin_model)

    def tearDown(self) -> None:
        self.request = None
        self.admin_model = None
        self.controller = None
        self.form = None

    def testExecute_return200_whenLoggedOut(self):
        # Arrange
        expected_result = {}

        # Act
        result = self.controller.execute(self.request)

        # Assert
        self.admin_model.logout_admin.assert_called_once()
        self.assertEqual(200, result.status_code)
        self.assertEqual(expected_result, json.loads(result.data))
