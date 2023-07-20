# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 20/07/23
from flask import Blueprint, request

from app.stuquiz.controllers.professor.add_professor_controller import AddProfessorController

add_professor_page = Blueprint('add_professor', __name__)


@add_professor_page.route('/professors', methods=['PUT'])
def add_professor():
    """Defines the route to add a new professor."""
    data = request.form
    professor_name = data['name'] if 'name' in data else None
    return AddProfessorController().execute({'name': professor_name})
