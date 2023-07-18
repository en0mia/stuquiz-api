# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 12/07/23
from flask import Blueprint, request

from app.stuquiz.controllers.university.update_university_controller import UpdateUniversityController

update_university_page = Blueprint('update_university', __name__)


@update_university_page.route('/universities/<university_id>', methods=['POST'])
def update_university(university_id=None):
    """Defines the route to update a university."""
    data = request.form
    university_name = data['name'] if 'name' in data else None
    return UpdateUniversityController().execute({'name': university_name, 'university_id': university_id})
