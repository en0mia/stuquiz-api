# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 05/07/23
from flask import Blueprint, request

from app.stuquiz.controllers.admin.login_admin_controller import LoginAdminController

login_admin_page = Blueprint('login_admin', __name__)


@login_admin_page.route('/admin/login', methods=['POST'])
def login():
    """Defines the route to log an admin in."""
    data = request.form
    email = data['email'] if 'email' in data else None
    password = data['password'] if 'password' in data else None

    return LoginAdminController().execute({'email': email, 'password': password})
