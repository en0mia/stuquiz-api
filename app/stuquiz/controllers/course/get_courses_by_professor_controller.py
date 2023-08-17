# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 19/07/23
import json
from typing import Optional

from easy_route.controllers.abstract_controller import AbstractController
from flask import Response, Request

from app.stuquiz.models.course.course_model import CourseModel


class GetCoursesByProfessorController(AbstractController):
    def __init__(self, course_model: Optional[CourseModel] = None):
        self.course_model = course_model or CourseModel()

    def execute(self, request: Request) -> Response:
        """
        :param request:
        :return: HTTP Response
        """
        courses = self.course_model.get_courses_by_professor(request.args['professor_id'])
        result = [course.dump() for course in courses]
        return Response(json.dumps(result), 200)
