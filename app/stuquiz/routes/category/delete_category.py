from easy_route.middlewares.data_validator_middleware import DataValidatorMiddleware
from easy_route.routes.route import Route
from flask import Blueprint, request
from validator_collection import checkers

from app.stuquiz.controllers.category.delete_category_controller import DeleteCategoryController
from app.stuquiz.middlewares.admin_login_middleware import AdminLoginMiddleware
from app.stuquiz.middlewares.data_providers.args_data_provider import ArgsDataProvider

delete_category_page = Blueprint('delete_category', __name__)

DATA_VALIDATION_RULES = {
    'category_id': checkers.is_uuid
}


@delete_category_page.route('/categories', methods=['DELETE'])
def delete_category():
    """Defines the route to delete a category."""
    return Route(request, DeleteCategoryController())\
        .add_middlewares([
            AdminLoginMiddleware(),
            DataValidatorMiddleware(DATA_VALIDATION_RULES, ArgsDataProvider())
        ]).dispatch()
