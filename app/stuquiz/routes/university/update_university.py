# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 12/07/23
from easy_route.middlewares.data_validator_middleware import DataValidatorMiddleware
from easy_route.routes.route import Route
from flask import Blueprint, request
from validator_collection import checkers

from app.stuquiz.controllers.university.update_university_controller import UpdateUniversityController
from app.stuquiz.middlewares.admin_login_middleware import AdminLoginMiddleware
from app.stuquiz.middlewares.data_providers.args_data_provider import ArgsDataProvider
from app.stuquiz.middlewares.data_providers.form_data_provider import FormDataProvider

update_university_page = Blueprint('update_university', __name__)

DATA_VALIDATION_RULES = {
    'university_id': checkers.is_uuid
}


@update_university_page.route('/university', methods=['POST'])
def update_university():
    """Defines the route to update a university."""
    middlewares = [
        AdminLoginMiddleware(),
        DataValidatorMiddleware({'university_id': checkers.is_uuid}, ArgsDataProvider()),
        DataValidatorMiddleware({'name': lambda name: checkers.is_string(name) and name}, FormDataProvider())
    ]
    return Route(request, UpdateUniversityController()) \
        .add_middlewares(middlewares).dispatch()
