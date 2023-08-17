# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 20/07/23
from easy_route.middlewares.data_validator_middleware import DataValidatorMiddleware
from easy_route.routes.route import Route
from flask import Blueprint, request
from validator_collection import checkers

from app.stuquiz.controllers.course.delete_course_controller import DeleteCourseController
from app.stuquiz.middlewares.admin_login_middleware import AdminLoginMiddleware
from app.stuquiz.middlewares.data_providers.args_data_provider import ArgsDataProvider

delete_course_page = Blueprint('delete_course', __name__)

DATA_VALIDATION_RULES = {
    'course_id': checkers.is_uuid
}


@delete_course_page.route('/course', methods=['DELETE'])
def delete_course():
    """Defines the route to delete a course."""
    return Route(request, DeleteCourseController())\
        .add_middlewares([AdminLoginMiddleware(), DataValidatorMiddleware(DATA_VALIDATION_RULES, ArgsDataProvider())])\
        .dispatch()
