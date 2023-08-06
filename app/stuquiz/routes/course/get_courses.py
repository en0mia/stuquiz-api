# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 18/07/23
from easy_route.routes.route import Route
from flask import Blueprint, request

from app.stuquiz.controllers.course.get_courses_controller import GetCoursesController

get_courses_page = Blueprint('get_courses', __name__)


@get_courses_page.route('/courses', methods=['GET'])
def get_courses():
    """Defines the route to get the courses."""
    return Route(request, GetCoursesController())\
        .dispatch()
