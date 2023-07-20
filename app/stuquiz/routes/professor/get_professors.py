# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 20/07/23
from flask import Blueprint

from app.stuquiz.controllers.professor.get_professors_controller import GetProfessorsController

get_professors_page = Blueprint('get_professors', __name__)


@get_professors_page.route('/professors', methods=['GET'])
def get_professors():
    """Defines the route to get the professors."""
    return GetProfessorsController().execute({})
