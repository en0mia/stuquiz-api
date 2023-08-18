from typing import Optional

from easy_route.controllers.abstract_controller import AbstractController
from flask import Response, Request

from app.stuquiz.models.category.category_model import CategoryModel


class DeleteCategoryController(AbstractController):
    def __init__(self, category_model: Optional[CategoryModel] = None):
        self.category_model = category_model or CategoryModel()

    def execute(self, request: Request) -> Response:
        """
        :param request:
        :return: HTTP Response
        """
        category = self.category_model.get_category_by_id(request.args['course_id'])

        if not category:
            return Response('', 404)

        if not self.category_model.delete_category(category):
            return Response('', 500)
        return Response('{}', 200)
