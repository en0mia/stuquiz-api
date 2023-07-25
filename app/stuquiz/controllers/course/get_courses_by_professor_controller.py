# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 19/07/23
import json
from typing import Optional

from flask import Response
from validator_collection import checkers

from app.stuquiz.controllers.abstract_controller import AbstractController
from app.stuquiz.models.course.course_model import CourseModel


class GetCoursesByProfessorController(AbstractController):
    def __init__(self, course_model: Optional[CourseModel] = None):
        self.course_model = course_model or CourseModel()

    def execute(self, data: dict) -> Response:
        """
        :param data: a dict containing the professor id
        :return: HTTP Response
        """
        professor_id = data['professor_id'] if 'professor_id' in data else None

        if not checkers.is_uuid(professor_id):
            return Response('', 400)
        courses = self.course_model.get_courses_by_professor(data['professor_id'])
        result = [course.dump() for course in courses]
        return Response(json.dumps(result), 200)
