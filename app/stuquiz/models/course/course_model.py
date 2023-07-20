# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 18/07/23
import uuid
from typing import Optional

from app.stuquiz.entities.course import Course
from app.stuquiz.repositories.course_repository import CourseRepository


class CourseModel(object):
    def __init__(self, course_repository: Optional[CourseRepository] = None):
        self.course_repository = course_repository or CourseRepository()

    def get_courses(self) -> list[Course]:
        """A proxy for CourseRepository.select_courses()
        :return: list[Course]
        """
        return self.course_repository.select_courses()

    def get_course_by_id(self, course_id: str) -> Optional[Course]:
        """A proxy for CourseRepository.select_course_by_id()
        :return: list[Course]
        """
        return self.course_repository.select_course_by_id(course_id)

    def get_courses_by_professor(self, professor_id: str) -> list[Course]:
        """A proxy for CourseRepository.select_courses_by_professor_id()
        :return: list[Course]
        """
        return self.course_repository.select_courses_by_professor_id(professor_id)

    def get_courses_by_category(self, category_id: str) -> list[Course]:
        """A proxy for CourseRepository.select_courses_by_category()
        :return: list[Course]
        """
        return self.course_repository.select_courses_by_category_id(category_id)

    def add_course(self, university_id: str, name: str, description: str, professor_id: str, code: str) -> bool:
        """A proxy for CourseRepository.create_course()
        :return: bool
        """
        course = Course(str(uuid.uuid4()), university_id, name, description, professor_id, code)
        return self.course_repository.create_course(course)

    def update_course(self, course_id: str, university_id: str, name: str, description: str, professor_id: str,
                      code: str) -> bool:
        """A proxy for CourseRepository.update_course()
        :return: bool
        """
        course = Course(course_id, university_id, name, description, professor_id, code)
        return self.course_repository.update_course(course)
