# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 20/07/23
import json
from typing import Optional

from flask import Response

from app.stuquiz.controllers.abstract_controller import AbstractController
from app.stuquiz.models.professor.professor_model import ProfessorModel


class GetProfessorsController(AbstractController):
    def __init__(self, professor_model: Optional[ProfessorModel] = None):
        self.professor_model = professor_model or ProfessorModel()

    def execute(self, data: dict) -> Response:
        """
        :param data: an empty dict
        :return: HTTP Response
        """
        professors = self.professor_model.get_professors()
        result = [professor.dump() for professor in professors]
        return Response(json.dumps(result), 200)
