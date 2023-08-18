from typing import Optional

from easy_route.controllers.abstract_controller import AbstractController
from flask import Response, Request

from app.stuquiz.models.admin.admin_model import AdminModel
from app.stuquiz.models.category.category_model import CategoryModel


class UpdateCategoryController(AbstractController):
    def __init__(self, category_model: Optional[CategoryModel] = None,
                 admin_model: Optional[AdminModel] = None):
        self.category_model = category_model or CategoryModel()
        self.admin_model = admin_model or AdminModel()

    def execute(self, request: Request) -> Response:
        """
        :param request:
        :return: HTTP Response
        """
        category = self.category_model.get_category_by_id(request.args['category_id'])

        if not category:
            return Response('', 404)

        category.name = request.form['name']

        if not self.category_model.update_category(category):
            return Response('', 500)
        return Response('{}', 200)
