# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 11/07/23
from easy_route.routes.route import Route
from flask import Blueprint, request

from app.stuquiz.controllers.admin.logout_admin_controller import LogoutAdminController
from app.stuquiz.middlewares.admin_login_middleware import AdminLoginMiddleware

logout_admin_page = Blueprint('logout_admin', __name__)


@logout_admin_page.route('/admin/logout', methods=['POST'])
def logout():
    """Defines the route to log out an admin."""
    return Route(request, LogoutAdminController()).add_middleware(AdminLoginMiddleware()).dispatch()
