# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 16/07/23
from easy_route.middlewares.data_validator_middleware import DataValidatorMiddleware
from easy_route.routes.route import Route
from flask import Blueprint, request
from validator_collection import checkers

from app.stuquiz.controllers.university.delete_university_controller import DeleteUniversityController
from app.stuquiz.middlewares.admin_login_middleware import AdminLoginMiddleware
from app.stuquiz.middlewares.data_providers.args_data_provider import ArgsDataProvider

delete_university_page = Blueprint('delete_university', __name__)

DATA_VALIDATION_RULES = {
    'university_id': checkers.is_uuid
}


@delete_university_page.route('/universities', methods=['DELETE'])
def delete_university():
    """Defines the route to delete a university."""
    return Route(request, DeleteUniversityController())\
        .add_middlewares([
            AdminLoginMiddleware(),
            DataValidatorMiddleware(DATA_VALIDATION_RULES, ArgsDataProvider())
        ]).dispatch()
