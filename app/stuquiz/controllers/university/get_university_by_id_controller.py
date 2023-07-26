# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 04/07/23
import json
from typing import Optional

from easy_route.controllers.abstract_controller import AbstractController
from flask import Response, Request

from app.stuquiz.models.university.university_model import UniversityModel


class GetUniversityByIdController(AbstractController):
    def __init__(self, university_model: Optional[UniversityModel] = None):
        self.university_model = university_model or UniversityModel()

    def execute(self, request: Request) -> Response:
        """
        :param request:
        :return: HTTP Response
        """
        university = self.university_model.get_university_by_id(request.args['university_id'])

        if not university:
            return Response('', 404)
        return Response(json.dumps(university.dump()), 200)
