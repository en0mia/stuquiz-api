# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 18/07/23
from typing import Optional

from app.stuquiz.entities.course import Course
from app.stuquiz.repositories.course_repository import CourseRepository


class CourseModel(object):
    def __init__(self, course_repository: Optional[CourseRepository] = None):
        self.course_repository = course_repository or CourseRepository()

    def get_courses(self) -> list[Course]:
        return self.course_repository.select_courses()