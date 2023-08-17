# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 11/07/23
from easy_route.middlewares.data_validator_middleware import DataValidatorMiddleware
from easy_route.routes.route import Route
from flask import Blueprint, request
from validator_collection import checkers

from app.stuquiz.controllers.university.add_university_controller import AddUniversityController
from app.stuquiz.middlewares.admin_login_middleware import AdminLoginMiddleware
from app.stuquiz.middlewares.data_providers.form_data_provider import FormDataProvider

add_university_page = Blueprint('add_university', __name__)

DATA_VALIDATION_RULES = {
    'name': lambda name: checkers.is_string(name) and name
}


@add_university_page.route('/universities', methods=['PUT'])
def add_university():
    """Defines the route to add a new universities."""
    return Route(request, AddUniversityController()) \
        .add_middlewares([AdminLoginMiddleware(), DataValidatorMiddleware(DATA_VALIDATION_RULES, FormDataProvider())])\
        .dispatch()
