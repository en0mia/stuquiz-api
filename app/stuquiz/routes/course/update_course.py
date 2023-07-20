# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 20/07/23
from flask import Blueprint, request

from app.stuquiz.controllers.course.update_course_controller import UpdateCourseController

update_course_page = Blueprint('update_course', __name__)


@update_course_page.route('/courses/<course_id>', methods=['POST'])
def update_course(course_id=None):
    """Defines the route to update a course."""
    data = request.form
    university_id = data['university_id'] if 'university_id' in data else None
    name = data['name'] if 'name' in data else None
    description = data['description'] if 'description' in data else None
    professor_id = data['professor_id'] if 'professor_id' in data else None
    code = data['code'] if 'code' in data else None

    return UpdateCourseController().execute({
        'course_id': course_id,
        'university_id': university_id,
        'name': name,
        'description': description,
        'professor_id': professor_id,
        'code': code
    })
