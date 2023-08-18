from easy_route.middlewares.data_validator_middleware import DataValidatorMiddleware
from easy_route.routes.route import Route
from flask import Blueprint, request
from validator_collection import checkers

from app.stuquiz.controllers.category.add_category_controller import AddCategoryController
from app.stuquiz.middlewares.admin_login_middleware import AdminLoginMiddleware
from app.stuquiz.middlewares.data_providers.form_data_provider import FormDataProvider

add_category_page = Blueprint('add_category', __name__)

DATA_VALIDATION_RULES = {
    'name': lambda name: checkers.is_string(name) and name
}


@add_category_page.route('/categories', methods=['PUT'])
def add_category():
    """Defines the route to add a new category."""
    return Route(request, AddCategoryController()) \
        .add_middlewares([AdminLoginMiddleware(), DataValidatorMiddleware(DATA_VALIDATION_RULES, FormDataProvider())])\
        .dispatch()
