# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 16/07/23
from flask import Blueprint

from app.stuquiz.controllers.university.delete_university_controller import DeleteUniversityController

delete_university_page = Blueprint('delete_university', __name__)


@delete_university_page.route('/universities/<university_id>', methods=['DELETE'])
def delete_university(university_id=None):
    """Defines the route to delete a university."""
    return DeleteUniversityController().execute({'university_id': university_id})
