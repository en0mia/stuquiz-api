# @author Lorenzo Varese
# @created 2023-06-30
from typing import Optional

from app.stuquiz.entities.category import Category
from app.stuquiz.entities.course import Course
from app.stuquiz.repositories.abstract_repository import AbstractRepository


class CourseRepository(AbstractRepository):
    def create_course(self, course: Course) -> bool:
        query = "INSERT INTO course (name, description, professor_id, code, university_id) VALUES (%s, %s, %s, %s, %s)"
        return self.insert(query, (course.name, course.description, course.professor_id, course.code,
                           course.university_id))

    def delete_course(self, course: Course) -> bool:
        query = "DELETE FROM course WHERE course_id = %s"
        return self.delete(query, (course.id, ))

    def update_course(self, course: Course) -> bool:
        query = "UPDATE course SET name = %s, description = %s, professor_id = %s, " \
                    "code = %s, university_id = %s WHERE id = %s"
        return self.update(query, (course.name, course.description, course.professor_id,
                           course.code, course.university_id, course.id))

    def select_course_by_id(self, course_id: str) -> Optional[Course]:
        query = "SELECT id, university_id, name, description, professor_id, code FROM course WHERE id = %s"
        result = self.select(query, (course_id,))
        course = Course(*result[0]) if result and len(result) > 0 else None

        if course:
            course.categories = self.select_course_categories(course.id)
        return course

    def select_course_categories(self, course_id: str) -> list[Category]:
        """Returns a list of categories linked to a course.
        :param course_id: The Course's ID.
        :return: list[Category]
        """
        query = "SELECT category.id, category.name FROM category, course, course_category " \
                "WHERE category.id = course_category.category_id " \
                "AND course.id = course_category.course_id AND course.id = %s"
        records = self.select(query, (course_id, ))
        return [Category(*record) for record in records] if records else []

    def select_courses_by_university_id(self, university_id: str) -> list[Course]:
        """Returns a list of courses linked to a university.
        :param university_id: The University's ID.
        :return: list[Course]
        """
        query = "SELECT id, university_id, name, description, professor_id, code FROM course WHERE university_id = %s"
        records = self.select(query, (university_id, ))
        results = [Course(*record) for record in records] if records else []

        for course in results:
            course.categories = self.select_course_categories(course.id)
        return results

    def select_courses(self) -> list[Course]:
        """Returns all the courses.
        TODO: implement pagination.
        :return: list[Course]
        """
        query = "SELECT id, university_id, name, description, professor_id, code FROM course"
        records = self.select(query, ())
        results = [Course(*record) for record in records] if records else []

        for course in results:
            course.categories = self.select_course_categories(course.id)
        return results

    def select_courses_by_professor_id(self, professor_id: str) -> list[Course]:
        """Returns the courses taught by Professor ID
        :param professor_id: The Professor's ID
        :return: list[Course]
        """
        query = "SELECT id, university_id, name, description, professor_id, code FROM course WHERE professor_id = %s"
        records = self.select(query, (professor_id,))
        results = [Course(*record) for record in records] if records else []

        for course in results:
            course.categories = self.select_course_categories(course.id)
        return results

    def select_courses_by_category_id(self, category_id: str) -> list[Course]:
        """Returns the courses tagged with the category_id
        :param category_id: The Category's ID
        :return: list[Course]
        """
        query = "SELECT course.id, course.university_id, course.name, course.description, course.professor_id, " \
                "course.code FROM category, course, course_category WHERE category.id = course_category.category_id " \
                "AND course.id = course_category.course_id AND category.id = %s"
        records = self.select(query, (category_id,))
        results = [Course(*record) for record in records] if records else []

        for course in results:
            course.categories = self.select_course_categories(course.id)
        return results
