# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 04/07/23
from easy_route.middlewares.data_validator_middleware import DataValidatorMiddleware
from easy_route.routes.route import Route
from flask import Blueprint, request
from validator_collection import checkers

from app.stuquiz.controllers.university.get_university_by_id_controller import GetUniversityByIdController
from app.stuquiz.middlewares.data_providers.args_data_provider import ArgsDataProvider

get_university_by_id_page = Blueprint('get_university_by_id_page', __name__)

DATA_VALIDATION_RULES = {
    'university_id': checkers.is_uuid
}


@get_university_by_id_page.route('/university', methods=['GET'])
def get_university_by_id():
    """Defines the route to get a university by id."""
    return Route(request, GetUniversityByIdController())\
        .add_middleware(DataValidatorMiddleware(DATA_VALIDATION_RULES, ArgsDataProvider()))\
        .dispatch()
