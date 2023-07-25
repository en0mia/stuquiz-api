# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 19/07/23
from flask import Blueprint, request

from app.stuquiz.controllers.course.add_course_controller import AddCourseController

add_course_page = Blueprint('add_course', __name__)


@add_course_page.route('/courses', methods=['PUT'])
def add_course():
    """Defines the route to add a new course."""
    data = request.form
    university_id = data['university_id'] if 'university_id' in data else None
    name = data['name'] if 'name' in data else None
    description = data['description'] if 'description' in data else None
    professor_id = data['professor_id'] if 'professor_id' in data else None
    code = data['code'] if 'code' in data else None

    return AddCourseController().execute({
        'university_id': university_id,
        'name': name,
        'description': description,
        'professor_id': professor_id,
        'code': code
    })
