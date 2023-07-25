# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 18/07/23
import json
from typing import Optional

from flask import Response

from app.stuquiz.controllers.abstract_controller import AbstractController
from app.stuquiz.models.course.course_model import CourseModel


class GetCoursesController(AbstractController):
    def __init__(self, course_model: Optional[CourseModel] = None):
        self.course_model = course_model or CourseModel()

    def execute(self, data: dict) -> Response:
        """
        :param data: an empty dict
        :return: HTTP Response
        """
        courses = self.course_model.get_courses()
        result = [course.dump() for course in courses]
        return Response(json.dumps(result), 200)
