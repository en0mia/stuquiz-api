# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 16/07/23
from typing import Optional

from easy_route.controllers.abstract_controller import AbstractController
from flask import Response, Request

from app.stuquiz.models.university.university_model import UniversityModel


class DeleteUniversityController(AbstractController):
    def __init__(self, university_model: Optional[UniversityModel] = None):
        self.university_model = university_model or UniversityModel()

    def execute(self, request: Request) -> Response:
        """
        :param request:
        :return: HTTP Response
        """
        university_id = request.args['university_id']
        university = self.university_model.get_university_by_id(university_id)

        if not university:
            return Response('', 404)

        if not self.university_model.delete_university(university):
            return Response('', 500)
        return Response('{}', 200)
