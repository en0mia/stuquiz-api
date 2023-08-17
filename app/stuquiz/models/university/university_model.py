# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 04/07/23
import uuid
from typing import Optional

from app.stuquiz.entities.course import Course
from app.stuquiz.entities.university import University
from app.stuquiz.repositories.course_repository import CourseRepository
from app.stuquiz.repositories.university_repository import UniversityRepository


class UniversityModel(object):
    def __init__(self, university_repository: Optional[UniversityRepository] = None,
                 course_repository: Optional[CourseRepository] = None):
        self.university_repository = university_repository or UniversityRepository()
        self.course_repository = course_repository or CourseRepository()

    def get_universities(self) -> list[University]:
        """A proxy for UniversityRepository.select_university()
        :return: A list of Universities.
        """
        return self.university_repository.select_universities()

    def get_university_by_id(self, university_id: str) -> Optional[University]:
        """A proxy for UniversityRepository.select_university_by_id()
        :return: University | None
        """
        return self.university_repository.select_university_by_id(university_id)

    def add_university(self, university_name: str) -> bool:
        """A proxy for UniversityRepository.create_university()
        :return: bool
        """
        university = University(str(uuid.uuid4()), university_name)

        return self.university_repository.create_university(university)

    def update_university(self, university: University) -> bool:
        """A proxy for UniversityRepository.update_university()
        :return: bool
        """
        return self.university_repository.update_university(university)

    def delete_university(self, university: University) -> bool:
        """A proxy for UniversityRepository.delete_university()
        :return: bool
        """
        return self.university_repository.delete_university(university)

    def get_university_courses(self, university: University) -> list[Course]:
        """A proxy for CourseRepository.select_courses_by_university_id()
        :return: list[Course]
        """
        return self.course_repository.select_courses_by_university_id(university.id)
