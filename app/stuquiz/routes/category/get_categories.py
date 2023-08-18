# @author Lorenzo Varese
# @created 2023-07-05

from easy_route.routes.route import Route
from flask import Blueprint, request

from app.stuquiz.controllers.category.get_categories_controller import GetCategoriesController

get_categories_page = Blueprint('get_categories', __name__)


@get_categories_page.route('/categories', methods=['GET'])
def get_categories():
    """Defines the route to get the categories."""
    return Route(request, GetCategoriesController()).dispatch()
