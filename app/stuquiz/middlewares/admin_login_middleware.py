# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 24/07/23
from typing import Optional

from easy_route.middlewares.abstract_middleware import AbstractMiddleware
from flask import Request, Response

from app.stuquiz.models.admin.admin_model import AdminModel


class AdminLoginMiddleware(AbstractMiddleware):
    """Checks if an admin is logged in."""
    def __init__(self, admin_model: Optional[AdminModel] = None):
        super().__init__()
        self.admin_model = admin_model or AdminModel()

    def dispatch(self, request: Request) -> Optional[Response]:
        """Returns HTTP 401 if the admin is not logged in, None otherwise.
        :param request: The route's request.
        :return: Response | None
        """
        if not self.admin_model.is_admin_logged_in():
            return Response('', 401)
        return None
