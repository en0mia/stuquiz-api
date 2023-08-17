# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 20/07/23
from typing import Optional

from easy_route.controllers.abstract_controller import AbstractController
from flask import Response, Request

from app.stuquiz.models.course.course_model import CourseModel
from app.stuquiz.models.university.university_model import UniversityModel


class UpdateCourseController(AbstractController):
    def __init__(self, course_model: Optional[CourseModel] = None, university_model: Optional[UniversityModel] = None):
        self.course_model = course_model or CourseModel()
        self.university_model = university_model or UniversityModel()

    def execute(self, request: Request) -> Response:
        """
        :param request:
        :return: HTTP Response
        """
        course_id = request.args['course_id']
        university_id = request.form['university_id']
        name = request.form['name']
        description = request.form['description']
        professor_id = request.form['professor_id']
        code = request.form['code']

        if not self.course_model.get_course_by_id(course_id):
            return Response('', 404)

        if not self.university_model.get_university_by_id(university_id):
            return Response('', 400)

        # TODO: Add check on Professor ID.

        if not self.course_model.update_course(course_id, university_id, name, description, professor_id, code):
            return Response('', 500)
        return Response('{}', 200)
