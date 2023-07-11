# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 11/07/23
from flask import Blueprint

from app.stuquiz.controllers.admin.logout_admin_controller import LogoutAdminController

logout_admin_page = Blueprint('logout_admin', __name__)


@logout_admin_page.route('/admin/logout', methods=['POST'])
def logout():
    """Defines the route to log out an admin."""
    return LogoutAdminController().execute({})
