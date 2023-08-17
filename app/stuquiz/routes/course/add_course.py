# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 19/07/23
from easy_route.middlewares.data_validator_middleware import DataValidatorMiddleware
from easy_route.routes.route import Route
from flask import Blueprint, request
from validator_collection import checkers

from app.stuquiz.controllers.course.add_course_controller import AddCourseController
from app.stuquiz.middlewares.admin_login_middleware import AdminLoginMiddleware
from app.stuquiz.middlewares.data_providers.form_data_provider import FormDataProvider

add_course_page = Blueprint('add_course', __name__)

DATA_VALIDATION_RULES = {
    'university_id': checkers.is_uuid,
    'name': lambda name: checkers.is_string(name) and name,
    'description': lambda description: checkers.is_string(description) and description,
    'professor_id': checkers.is_uuid,
    'code': lambda code: checkers.is_string(code) and code
}


@add_course_page.route('/courses', methods=['PUT'])
def add_course():
    """Defines the route to add a new course."""
    return Route(request, AddCourseController())\
        .add_middlewares([AdminLoginMiddleware(), DataValidatorMiddleware(DATA_VALIDATION_RULES, FormDataProvider())])\
        .dispatch()
