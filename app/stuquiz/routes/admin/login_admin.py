# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 05/07/23
from easy_route.middlewares.data_validator_middleware import DataValidatorMiddleware
from easy_route.routes.route import Route
from flask import Blueprint, request
from validator_collection import checkers

from app.stuquiz.controllers.admin.login_admin_controller import LoginAdminController
from app.stuquiz.middlewares.data_providers.form_data_provider import FormDataProvider

login_admin_page = Blueprint('login_admin', __name__)

DATA_VALIDATION_RULES = {
    'email': checkers.is_email,
    'password': checkers.is_string
}


@login_admin_page.route('/admin/login', methods=['POST'])
def login():
    """Defines the route to log an admin in."""
    return Route(request, LoginAdminController())\
        .add_middleware(DataValidatorMiddleware(DATA_VALIDATION_RULES, FormDataProvider())).dispatch()
