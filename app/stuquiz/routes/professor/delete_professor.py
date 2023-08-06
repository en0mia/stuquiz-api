# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 20/07/23
from flask import Blueprint

from app.stuquiz.controllers.professor.delete_professor_controller import DeleteProfessorController

delete_professor_page = Blueprint('delete_professor', __name__)


@delete_professor_page.route('/professors/<professor_id>', methods=['DELETE'])
def delete_professor(professor_id=None):
    """Defines the route to delete a professor."""
    return DeleteProfessorController().execute({'professor_id': professor_id})
