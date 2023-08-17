# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 19/07/23
from easy_route.middlewares.data_validator_middleware import DataValidatorMiddleware
from easy_route.routes.route import Route
from flask import Blueprint, request
from validator_collection import checkers

from app.stuquiz.controllers.course.get_courses_by_category_controller import GetCoursesByCategoryController
from app.stuquiz.middlewares.data_providers.args_data_provider import ArgsDataProvider

get_courses_by_category_page = Blueprint('get_courses_by_category_page', __name__)

DATA_VALIDATION_RULES = {
    'category_id': checkers.is_uuid
}


@get_courses_by_category_page.route('/courses/category', methods=['GET'])
def get_course_by_category():
    """Defines the route to get the courses by Category ID."""
    return Route(request, GetCoursesByCategoryController())\
        .add_middleware(DataValidatorMiddleware(DATA_VALIDATION_RULES, ArgsDataProvider()))\
        .dispatch()
