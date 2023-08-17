# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 16/07/23
from easy_route.middlewares.data_validator_middleware import DataValidatorMiddleware
from easy_route.routes.route import Route
from flask import Blueprint, request
from validator_collection import checkers

from app.stuquiz.controllers.university.get_university_courses_controller import GetUniversityCoursesController
from app.stuquiz.middlewares.data_providers.args_data_provider import ArgsDataProvider

get_university_courses_page = Blueprint('get_university_courses', __name__)

DATA_VALIDATION_RULES = {
    'university_id': checkers.is_uuid
}


@get_university_courses_page.route('/university/courses', methods=['GET'])
def get_university_courses():
    """Defines the route to get the courses linked to a university."""
    return Route(request, GetUniversityCoursesController())\
        .add_middleware(DataValidatorMiddleware(DATA_VALIDATION_RULES, ArgsDataProvider())).dispatch()
