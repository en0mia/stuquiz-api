# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 18/07/23
from easy_route.middlewares.data_validator_middleware import DataValidatorMiddleware
from easy_route.routes.route import Route
from flask import Blueprint, request
from validator_collection import checkers

from app.stuquiz.controllers.course.get_course_by_id_controller import GetCourseByIdController
from app.stuquiz.middlewares.data_providers.args_data_provider import ArgsDataProvider

get_course_by_id_page = Blueprint('get_course_by_id_page', __name__)

DATA_VALIDATION_RULES = {
    'course_id': checkers.is_uuid
}


@get_course_by_id_page.route('/course', methods=['GET'])
def get_course_by_id():
    """Defines the route to get a course by id."""
    return Route(request, GetCourseByIdController()) \
        .add_middlewares([DataValidatorMiddleware(DATA_VALIDATION_RULES, ArgsDataProvider())]) \
        .dispatch()
