# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 20/07/23
from typing import Optional

from flask import Response
from validator_collection import checkers

from app.stuquiz.controllers.abstract_controller import AbstractController
from app.stuquiz.models.admin.admin_model import AdminModel
from app.stuquiz.models.course.course_model import CourseModel
from app.stuquiz.models.university.university_model import UniversityModel


class UpdateCourseController(AbstractController):
    def __init__(self, course_model: Optional[CourseModel] = None, admin_model: Optional[AdminModel] = None,
                 university_model: Optional[UniversityModel] = None):
        self.course_model = course_model or CourseModel()
        self.admin_model = admin_model or AdminModel()
        self.university_model = university_model or UniversityModel()

    def execute(self, data: dict) -> Response:
        """
        :param data: a dict containing the course information.
        :return: HTTP Response
        """
        if not self.admin_model.is_admin_logged_in():
            return Response('', 401)

        course_id = data['course_id'] if 'course_id' in data else None
        university_id = data['university_id'] if 'university_id' in data else None
        name = data['name'] if 'name' in data else None
        description = data['description'] if 'description' in data else None
        professor_id = data['professor_id'] if 'professor_id' in data else None
        code = data['code'] if 'code' in data else None

        if not checkers.is_uuid(course_id) or not checkers.is_uuid(university_id) or not checkers.is_string(name) \
                or not name or not checkers.is_string(description) or not description \
                or not checkers.is_uuid(professor_id) or not checkers.is_string(code) or not code:
            return Response('', 400)

        if not self.course_model.get_course_by_id(course_id):
            return Response('', 404)

        if not self.university_model.get_university_by_id(university_id):
            return Response('', 400)

        # TODO: Add check on Professor ID.

        if not self.course_model.update_course(course_id, university_id, name, description, professor_id, code):
            return Response('', 500)
        return Response('{}', 200)
