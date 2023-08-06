# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 19/07/23
from easy_route.middlewares.data_validator_middleware import DataValidatorMiddleware
from easy_route.routes.route import Route
from flask import Blueprint, request
from validator_collection import checkers

from app.stuquiz.controllers.course.get_courses_by_professor_controller import GetCoursesByProfessorController
from app.stuquiz.middlewares.data_providers.args_data_provider import ArgsDataProvider

get_courses_by_professor_page = Blueprint('get_courses_by_professor_page', __name__)

DATA_VALIDATION_RULES = {
    'professor_id': checkers.is_uuid
}


@get_courses_by_professor_page.route('/courses/professor', methods=['GET'])
def get_course_by_professor():
    """Defines the route to get the courses by Professor ID."""
    return Route(request, GetCoursesByProfessorController())\
        .add_middleware(DataValidatorMiddleware(DATA_VALIDATION_RULES, ArgsDataProvider()))\
        .dispatch()
