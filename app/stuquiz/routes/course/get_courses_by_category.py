# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 19/07/23
from flask import Blueprint

from app.stuquiz.controllers.course.get_courses_by_category_controller import GetCoursesByCategoryController

get_courses_by_category_page = Blueprint('get_courses_by_category_page', __name__)


@get_courses_by_category_page.route('/courses/category/<category_id>', methods=['GET'])
def get_course_by_category(category_id=None):
    """Defines the route to get the courses by Category ID."""
    return GetCoursesByCategoryController().execute({'category_id': category_id})
