# @author Lorenzo Varese
# @created 2023-07-05


from flask import Blueprint

from app.stuquiz.controllers.category.get_category_by_id_controller import GetCategoryByIdController

get_category_by_id_page = Blueprint('get_category_by_id', __name__)


@get_category_by_id_page.route('/categories/<category_id>', methods=['GET'])
def get_category_by_id(category_id=None):
    """Defines the route to get a category by id."""
    return GetCategoryByIdController().execute({'category_id': category_id})
