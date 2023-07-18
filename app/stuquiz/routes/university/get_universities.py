# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 04/07/23
from flask import Blueprint

from app.stuquiz.controllers.university.get_universities_controller import GetUniversitiesController

get_universities_page = Blueprint('get_universities', __name__)


@get_universities_page.route('/universities', methods=['GET'])
def get_universities():
    """Defines the route to get the universities."""
    return GetUniversitiesController().execute({})
