# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 11/07/23
from typing import Optional

from easy_route.controllers.abstract_controller import AbstractController
from flask import Response, Request

from app.stuquiz.models.admin.admin_model import AdminModel


class LogoutAdminController(AbstractController):
    """Logs the admin out by removing the session cookie."""
    def __init__(self, admin_model: Optional[AdminModel] = None):
        self.admin_model = admin_model or AdminModel()

    def execute(self, request: Request) -> Response:
        """
        :param request:
        :return: HTTPResponse
        """
        self.admin_model.logout_admin()
        return Response('{}', 200)
