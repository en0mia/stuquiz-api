# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 04/07/23
import json
from typing import Optional

from flask import Response

from app.stuquiz.controllers.abstract_controller import AbstractController
from app.stuquiz.models.university.university_model import UniversityModel


class GetUniversitiesController(AbstractController):
    def __init__(self, university_model: Optional[UniversityModel] = None):
        self.university_model = university_model or UniversityModel()

    def execute(self, data: dict) -> Response:
        """
        :param data: an empty dict
        :return: HTTP Response
        """
        universities = self.university_model.get_universities()
        result = []

        for university in universities:
            result.append(university.dump())
        return Response(json.dumps(result), 200)
