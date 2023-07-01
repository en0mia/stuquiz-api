# @author Lorenzo Varese
# @created 2023-06-30

from app.stuquiz.repositories.abstract_repository import AbstractRepository
from app.stuquiz.entities.course import Course


class CourseRepository(AbstractRepository):

    def create_course(self, course: Course) -> bool:
        query = "INSERT INTO course (name, description, professor, code, university_id) VALUES (%s, %s, %s, %s, %s)"
        return self.insert(query, (course.name, course.description, course.professor, course.code,
                           course.university_id))

    def delete_course(self, course: Course) -> bool:
        query = "DELETE FROM course WHERE course_id = %s"
        return self.delete(query, course.id)

    def update_course(self, course: Course) -> bool:
        query = "UPDATE course SET name = %s, description = %s, professor = %s, " \
                    "code = %s, university_id = %s WHERE id = %s"
        return self.update(query, (course.name, course.description, course.professor,
                           course.code, course.university_id, course.id))

    def select_course_by_id(self, course_id: int) -> Course:
        query = "SELECT * FROM course WHERE id = %s"
        result = self.select(query, course_id)
        return Course(*result[0]) if result and len(result) > 0 else None
