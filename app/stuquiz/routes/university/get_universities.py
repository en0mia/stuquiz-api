# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 04/07/23
from easy_route.routes.route import Route
from flask import Blueprint, request

from app.stuquiz.controllers.university.get_universities_controller import GetUniversitiesController

get_universities_page = Blueprint('get_universities', __name__)


@get_universities_page.route('/universities', methods=['GET'])
def get_universities():
    """Defines the route to get the universities."""
    return Route(request, GetUniversitiesController()).dispatch()
