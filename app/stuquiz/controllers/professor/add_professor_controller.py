# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 20/07/23
from typing import Optional

from flask import Response
from validator_collection import checkers

from app.stuquiz.controllers.abstract_controller import AbstractController
from app.stuquiz.models.admin.admin_model import AdminModel
from app.stuquiz.models.professor.professor_model import ProfessorModel


class AddProfessorController(AbstractController):
    def __init__(self, professor_model: Optional[ProfessorModel] = None, admin_model: Optional[AdminModel] = None):
        self.professor_model = professor_model or ProfessorModel()
        self.admin_model = admin_model or AdminModel()

    def execute(self, data: dict) -> Response:
        """
        :param data: a dict containing the professor name.
        :return: HTTP Response
        """
        if not self.admin_model.is_admin_logged_in():
            return Response('', 401)

        professor_name = data['name'] if 'name' in data else None

        if not checkers.is_string(professor_name) or not professor_name:
            return Response('', 400)

        if not self.professor_model.add_professor(professor_name):
            return Response('', 500)
        return Response('{}', 200)
