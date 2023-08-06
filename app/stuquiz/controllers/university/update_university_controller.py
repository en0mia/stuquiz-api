# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 12/07/23
from typing import Optional

from easy_route.controllers.abstract_controller import AbstractController
from flask import Response, Request

from app.stuquiz.models.admin.admin_model import AdminModel
from app.stuquiz.models.university.university_model import UniversityModel


class UpdateUniversityController(AbstractController):
    def __init__(self, university_model: Optional[UniversityModel] = None,
                 admin_model: Optional[AdminModel] = None):
        self.university_model = university_model or UniversityModel()
        self.admin_model = admin_model or AdminModel()

    def execute(self, request: Request) -> Response:
        """
        :param request:
        :return: HTTP Response
        """
        university = self.university_model.get_university_by_id(request.args['university_id'])

        if not university:
            return Response('', 404)

        university.name = request.form['name']

        if not self.university_model.update_university(university):
            return Response('', 500)
        return Response('{}', 200)
