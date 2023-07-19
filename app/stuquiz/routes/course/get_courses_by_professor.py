# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 19/07/23
from flask import Blueprint

from app.stuquiz.controllers.course.get_courses_by_professor_controller import GetCoursesByProfessorController

get_courses_by_professor_page = Blueprint('get_courses_by_professor_page', __name__)


@get_courses_by_professor_page.route('/courses/professor/<professor_id>', methods=['GET'])
def get_course_by_professor(professor_id=None):
    """Defines the route to get the courses by Professor ID."""
    return GetCoursesByProfessorController().execute({'professor_id': professor_id})
