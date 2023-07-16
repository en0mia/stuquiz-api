# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 16/07/23
import json
from typing import Optional

from flask import Response
from validator_collection import checkers

from app.stuquiz.controllers.abstract_controller import AbstractController
from app.stuquiz.models.university.university_model import UniversityModel


class GetUniversityCoursesController(AbstractController):
    def __init__(self, university_model: Optional[UniversityModel] = None):
        self.university_model = university_model or UniversityModel()

    def execute(self, data: dict) -> Response:
        """
        :param data: a dict containing the university id.
        :return: HTTP Response
        """
        university_id = data['university_id'] if 'university_id' in data else None

        if not checkers.is_uuid(university_id):
            return Response('', 400)
        university = self.university_model.get_university_by_id(data['university_id'])

        if not university:
            return Response('', 404)
        courses = self.university_model.get_university_courses(university)
        result = [course.dump() for course in courses]
        return Response(json.dumps(result), 200)
