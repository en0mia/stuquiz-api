# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 20/07/23
from typing import Optional

from flask import Response
from validator_collection import checkers

from app.stuquiz.controllers.abstract_controller import AbstractController
from app.stuquiz.models.admin.admin_model import AdminModel
from app.stuquiz.models.course.course_model import CourseModel


class DeleteCourseController(AbstractController):
    def __init__(self, course_model: Optional[CourseModel] = None, admin_model: Optional[AdminModel] = None):
        self.course_model = course_model or CourseModel()
        self.admin_model = admin_model or AdminModel()

    def execute(self, data: dict) -> Response:
        """
        :param data: a dict containing the course ID.
        :return: HTTP Response
        """
        if not self.admin_model.is_admin_logged_in():
            return Response('', 401)

        course_id = data['course_id'] if 'course_id' in data else None

        if not checkers.is_uuid(course_id):
            return Response('', 400)

        course = self.course_model.get_course_by_id(course_id)

        if not course:
            return Response('', 404)

        if not self.course_model.delete_course(course):
            return Response('', 500)
        return Response('{}', 200)
