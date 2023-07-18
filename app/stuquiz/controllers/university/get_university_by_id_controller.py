# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 04/07/23
import json
from typing import Optional

from flask import Response
from validator_collection import checkers

from app.stuquiz.controllers.abstract_controller import AbstractController
from app.stuquiz.models.university.university_model import UniversityModel


class GetUniversityByIdController(AbstractController):
    def __init__(self, university_model: Optional[UniversityModel] = None):
        self.university_model = university_model or UniversityModel()

    def execute(self, data: dict) -> Response:
        """
        :param data: a dict containing the university id
        :return: HTTP Response
        """
        university_id = data['university_id']

        if not checkers.is_uuid(university_id):
            return Response('', 400)
        university = self.university_model.get_university_by_id(data['university_id'])

        if not university:
            return Response('', 404)
        return Response(json.dumps(university.dump()), 200)
