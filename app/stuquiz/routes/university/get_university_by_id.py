# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 04/07/23
from flask import Blueprint

from app.stuquiz.controllers.university.get_university_by_id_controller import GetUniversityByIdController

get_university_by_id_page = Blueprint('get_university_by_id_page', __name__)


@get_university_by_id_page.route('/universities/<university_id>', methods=['GET'])
def get_university_by_id(university_id=None):
    """Defines the route to get a university by id."""
    return GetUniversityByIdController().execute({'university_id': university_id})
