# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 18/07/23
from flask import Blueprint

from app.stuquiz.controllers.course.get_course_by_id_controller import GetCourseByIdController

get_course_by_id_page = Blueprint('get_course_by_id_page', __name__)


@get_course_by_id_page.route('/courses/<course_id>', methods=['GET'])
def get_course_by_id(course_id=None):
    """Defines the route to get a course by id."""
    return GetCourseByIdController().execute({'course_id': course_id})
