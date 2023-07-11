# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 11/07/23
from typing import Optional

from flask import Response

from app.stuquiz.controllers.abstract_controller import AbstractController
from app.stuquiz.models.admin.admin_model import AdminModel


class LogoutAdminController(AbstractController):
    def __init__(self, admin_model: Optional[AdminModel] = None):
        self.admin_model = admin_model or AdminModel()

    def execute(self, data: dict) -> Response:
        if not self.admin_model.is_admin_logged_in():
            return Response('', 401)
        self.admin_model.logout_admin()
        return Response('{}', 200)
