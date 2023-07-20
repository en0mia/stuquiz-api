# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 20/07/23
from flask import Blueprint, request

from app.stuquiz.controllers.professor.update_professor_controller import UpdateProfessorController

update_professor_page = Blueprint('update_professor', __name__)


@update_professor_page.route('/professors/<professor_id>', methods=['POST'])
def update_professor(professor_id=None):
    """Defines the route to update a professor."""
    data = request.form
    professor_name = data['name'] if 'name' in data else None
    return UpdateProfessorController().execute({'professor_id': professor_id, 'name': professor_name})
