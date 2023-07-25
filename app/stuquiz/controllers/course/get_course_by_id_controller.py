# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 18/07/23
import json
from typing import Optional

from flask import Response
from validator_collection import checkers

from app.stuquiz.controllers.abstract_controller import AbstractController
from app.stuquiz.models.course.course_model import CourseModel


class GetCourseByIdController(AbstractController):
    def __init__(self, course_model: Optional[CourseModel] = None):
        self.course_model = course_model or CourseModel()

    def execute(self, data: dict) -> Response:
        """
        :param data: a dict containing the course id
        :return: HTTP Response
        """
        course_id = data['course_id'] if 'course_id' in data else None

        if not checkers.is_uuid(course_id):
            return Response('', 400)
        course = self.course_model.get_course_by_id(data['course_id'])

        if not course:
            return Response('', 404)
        return Response(json.dumps(course.dump()), 200)
