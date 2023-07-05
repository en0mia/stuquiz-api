# @author Lorenzo Varese
# @created 2023-07-05


import json
from typing import Optional

from flask import Response
from validator_collection import checkers

from app.stuquiz.controllers.abstract_controller import AbstractController
from app.stuquiz.models.category.category_model import CategoryModel


class GetCategoryByIdController(AbstractController):
    """Returns category by id."""
    def __init__(self, category_model: Optional[CategoryModel] = None):
        self.category_model = category_model or CategoryModel()

    def execute(self, data: dict) -> Response:
        """
        :param data: a dict containing the category id
        :return: HTTP Response
        """
        category_id = data['category_id']

        if not checkers.is_uuid(category_id):
            return Response('', 400)
        category = self.category_model.get_category_by_id(data['category_id'])

        if not category:
            return Response('', 404)
        return Response(json.dumps(category.dump()), 200)
