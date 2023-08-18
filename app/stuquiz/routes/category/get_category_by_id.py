# @author Lorenzo Varese
# @created 2023-07-05

from easy_route.middlewares.data_validator_middleware import DataValidatorMiddleware
from easy_route.routes.route import Route
from flask import Blueprint, request
from validator_collection import checkers

from app.stuquiz.controllers.category.get_category_by_id_controller import GetCategoryByIdController
from app.stuquiz.middlewares.data_providers.args_data_provider import ArgsDataProvider

get_category_by_id_page = Blueprint('get_category_by_id', __name__)

DATA_VALIDATION_RULES = {
    'category_id': checkers.is_uuid
}


@get_category_by_id_page.route('/category', methods=['GET'])
def get_category_by_id():
    """Defines the route to get a category by id."""
    return Route(request, GetCategoryByIdController())\
        .add_middleware(DataValidatorMiddleware(DATA_VALIDATION_RULES, ArgsDataProvider()))\
        .dispatch()
