# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 05/07/23
from typing import Optional

from easy_route.controllers.abstract_controller import AbstractController
from flask import Response, Request

from app.stuquiz.models.admin.admin_model import AdminModel


class LoginAdminController(AbstractController):
    """Logs the admin in and store the user_id into the cookie session managed by the client."""
    def __init__(self, admin_model: Optional[AdminModel] = None):
        self.admin_model = admin_model or AdminModel()

    def execute(self, request: Request) -> Response:
        """
        :param request:
        :return: HTTP Response.
        """
        email = request.form['email']
        clear_password = request.form['password']

        admin_id = self.admin_model.login_admin(email, clear_password)

        if admin_id is None:
            return Response('', 401)
        self.admin_model.store_session(admin_id)
        return Response('', 200)
