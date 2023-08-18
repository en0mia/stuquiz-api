from typing import Optional

from easy_route.controllers.abstract_controller import AbstractController
from flask import Response, Request

from app.stuquiz.models.category.category_model import CategoryModel


class AddCategoryController(AbstractController):
    def __init__(self, category_model: Optional[CategoryModel] = None):
        self.category_model = category_model or CategoryModel()

    def execute(self, request: Request) -> Response:
        """
        :param request:
        :return: HTTP Response
        """
        name = request.form['name']

        if not self.category_model.add_category(name):
            return Response('', 500)
        return Response('{}', 200)
