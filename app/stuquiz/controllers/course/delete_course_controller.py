# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 20/07/23
from typing import Optional

from easy_route.controllers.abstract_controller import AbstractController
from flask import Response, Request

from app.stuquiz.models.course.course_model import CourseModel


class DeleteCourseController(AbstractController):
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

        if not self.course_model.delete_course(course):
            return Response('', 500)
        return Response('{}', 200)
