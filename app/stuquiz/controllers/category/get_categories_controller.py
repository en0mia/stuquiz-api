# @author Lorenzo Varese
# @created 2023-07-05


import json
from typing import Optional

from flask import Response, make_response

from app.stuquiz.controllers.abstract_controller import AbstractController
from app.stuquiz.models.category.category_model import CategoryModel


class GetCategoriesController(AbstractController):
    """Returns all the categories."""
    def __init__(self, category_model: Optional[CategoryModel] = None):
        self.category_model = category_model or CategoryModel()

    def execute(self, data: dict) -> Response:
        """
        :param data: an empty dict
        :return: HTTP Response
        """
        categories = self.category_model.get_categories()
        result = []

        for category in categories:
            result.append(category.dump())
        return Response(json.dumps(result), 200)
