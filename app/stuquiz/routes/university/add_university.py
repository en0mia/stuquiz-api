# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 11/07/23
from flask import Blueprint, request

from app.stuquiz.controllers.university.add_university_controller import AddUniversityController

add_university_page = Blueprint('add_university', __name__)


@add_university_page.route('/universities', methods=['PUT'])
def add_university():
    """Defines the route to add a new universities."""
    data = request.form
    university_name = data['name'] if 'name' in data else None
    return AddUniversityController().execute({'name': university_name})
