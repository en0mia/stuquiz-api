from easy_route.middlewares.data_validator_middleware import DataValidatorMiddleware
from easy_route.routes.route import Route
from flask import Blueprint, request
from validator_collection import checkers

from app.stuquiz.controllers.category.update_category_controller import UpdateCategoryController
from app.stuquiz.middlewares.admin_login_middleware import AdminLoginMiddleware
from app.stuquiz.middlewares.data_providers.args_data_provider import ArgsDataProvider
from app.stuquiz.middlewares.data_providers.form_data_provider import FormDataProvider

update_category_page = Blueprint('update_category', __name__)

DATA_VALIDATION_RULES = {
    'category_id': checkers.is_uuid
}


@update_category_page.route('/category', methods=['POST'])
def update_category():
    """Defines the route to update a category."""
    middlewares = [
        AdminLoginMiddleware(),
        DataValidatorMiddleware({'category_id': checkers.is_uuid}, ArgsDataProvider()),
        DataValidatorMiddleware({'name': lambda name: checkers.is_string(name) and name}, FormDataProvider())
    ]
    return Route(request, UpdateCategoryController()) \
        .add_middlewares(middlewares).dispatch()
