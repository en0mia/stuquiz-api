# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 11/07/23
from typing import Optional

from easy_route.controllers.abstract_controller import AbstractController
from flask import Response, Request

from app.stuquiz.models.university.university_model import UniversityModel


class AddUniversityController(AbstractController):
    def __init__(self, university_model: Optional[UniversityModel] = None):
        self.university_model = university_model or UniversityModel()

    def execute(self, request: Request) -> Response:
        """
        :param request:
        :return: HTTP Response
        """
        if not self.university_model.add_university(request.form['name']):
            return Response('', 500)
        return Response('{}', 200)
