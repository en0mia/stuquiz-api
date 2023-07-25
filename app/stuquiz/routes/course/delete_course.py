# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 20/07/23
from flask import Blueprint

from app.stuquiz.controllers.course.delete_course_controller import DeleteCourseController

delete_course_page = Blueprint('delete_course', __name__)


@delete_course_page.route('/courses/<course_id>', methods=['DELETE'])
def delete_course(course_id=None):
    """Defines the route to delete a course."""
    return DeleteCourseController().execute({'course_id': course_id})
