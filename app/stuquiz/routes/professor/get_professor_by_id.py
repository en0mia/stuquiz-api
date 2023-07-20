# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 20/07/23
from flask import Blueprint

from app.stuquiz.controllers.professor.get_professor_by_id_controller import GetProfessorByIdController

get_professor_by_id_page = Blueprint('get_professor_by_id', __name__)


@get_professor_by_id_page.route('/professors/<professor_id>', methods=['GET'])
def get_professor_by_id(professor_id=None):
    """Defines the route to get a professor by id."""
    return GetProfessorByIdController().execute({'professor_id': professor_id})
