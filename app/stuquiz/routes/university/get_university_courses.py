# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 16/07/23
from flask import Blueprint

from app.stuquiz.controllers.university.get_university_courses_controller import GetUniversityCoursesController

get_university_courses_page = Blueprint('get_university_courses', __name__)


@get_university_courses_page.route('/universities/<university_id>/courses', methods=['GET'])
def get_university_courses(university_id=None):
    """Defines the route to get the courses linked to a university."""
    return GetUniversityCoursesController().execute({'university_id': university_id})
