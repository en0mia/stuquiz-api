# @author Lorenzo Varese
# @created 2023-07-05
import json
from typing import Optional

from easy_route.controllers.abstract_controller import AbstractController
from flask import Response, Request

from app.stuquiz.models.category.category_model import CategoryModel


class GetCategoriesController(AbstractController):
    def __init__(self, category_model: Optional[CategoryModel] = None):
        self.category_model = category_model or CategoryModel()

    def execute(self, request: Request) -> Response:
        """
        :param request:
        :return: HTTP Response
        """
        categories = self.category_model.get_categories()
        result = [category.dump() for category in categories]
        return Response(json.dumps(result), 200)