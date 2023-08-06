# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 18/07/23
import json
from typing import Optional

from easy_route.controllers.abstract_controller import AbstractController
from flask import Response, Request

from app.stuquiz.models.course.course_model import CourseModel


class GetCourseByIdController(AbstractController):
    def __init__(self, course_model: Optional[CourseModel] = None):
        self.course_model = course_model or CourseModel()

    def execute(self, request: Request) -> Response:
        """
        :param request:
        :return: HTTP Response
        """
        course = self.course_model.get_course_by_id(request.args['course_id'])

        if not course:
            return Response('', 404)
        return Response(json.dumps(course.dump()), 200)
