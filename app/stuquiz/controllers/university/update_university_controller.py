# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 12/07/23
from typing import Optional

from flask import Response
from validator_collection import checkers

from app.stuquiz.controllers.abstract_controller import AbstractController
from app.stuquiz.models.admin.admin_model import AdminModel
from app.stuquiz.models.university.university_model import UniversityModel


class UpdateUniversityController(AbstractController):
    def __init__(self, university_model: Optional[UniversityModel] = None,
                 admin_model: Optional[AdminModel] = None):
        self.university_model = university_model or UniversityModel()
        self.admin_model = admin_model or AdminModel()

    def execute(self, data: dict) -> Response:
        """
        :param data: a dict containing the university id and the new name.
        :return: HTTP Response
        """
        if not self.admin_model.is_admin_logged_in():
            return Response('', 401)

        university_id = data['university_id'] if 'university_id' in data else None
        university_name = data['name'] if 'name' in data else None

        if not checkers.is_string(university_name) or not checkers.is_not_empty(university_name) \
                or not checkers.is_uuid(university_id):
            return Response('', 400)

        university = self.university_model.get_university_by_id(university_id)

        if not university:
            return Response('', 404)

        university.name = university_name

        if not self.university_model.update_university(university):
            return Response('', 500)
        return Response('{}', 200)
