# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 05/07/23
from typing import Optional

from flask import Response
from validator_collection import checkers

from app.stuquiz.controllers.abstract_controller import AbstractController
from app.stuquiz.models.admin.admin_model import AdminModel


class LoginAdminController(AbstractController):
    """Logs the admin in and store the user_id into the cookie session managed by the client."""
    def __init__(self, admin_model: Optional[AdminModel] = None):
        self.admin_model = admin_model or AdminModel()

    def execute(self, data: dict) -> Response:
        """
        :param data: a dict containing email and clear text password for the admin.
        :return: HTTP Response.
        """
        email = data['email']
        clear_password = data['password']

        if not checkers.is_email(email) or not clear_password:
            return Response('', 400)

        admin_id = self.admin_model.login_admin(email, clear_password)

        if admin_id is None:
            return Response('', 401)
        self.admin_model.store_session(admin_id)
        return Response('', 200)
