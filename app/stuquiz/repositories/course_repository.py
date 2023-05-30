from app.stuquiz.repositories.abstract_repository import Repository
from app.stuquiz.entities.course import Course


class CourseRepository(Repository):

    def insert(self, course: Course) -> bool:
        try:
            query = "INSERT INTO course (name, description, professor, code, university_id) VALUES (%s, %s, %s, %s, %s)"
            values = (course.name, course.description, course.professor, course.code, course.university_id)

            cursor = self.db.cursor()
            cursor.execute(query, values)
            self.db.commit()

            for category in course.categories:
                query = "INSERT INTO course_category (course_id, category_id) VALUES (%s, %s)"
                values = (course.uuid, category.uuid)

                cursor = self.db.cursor()
                cursor.execute(query, values)
                self.db.commit()

        except Exception as e:
            print("Error inserting course:", e)
            self.db.rollback()
            return False

        return True

    def delete(self, course: Course) -> bool:
        try:
            query = "DELETE FROM course WHERE course_id = %s"
            values = (course.id,)
            cursor = self.db.cursor()
            cursor.execute(query, values)
            self.db.commit()

        except Exception as e:
            print("Error deleting course:", e)
            self.db.rollback()
            return False

        return True

    def update(self, course: Course) -> bool:
        try:
            query = "UPDATE course SET name = %s, description = %s, professor = %s, " \
                    "code = %s, university_id = %s WHERE id = %s"
            values = (course.name, course.description, course.professor, course.code, course.university_id, course.id)

            cursor = self.db.cursor()
            cursor.execute(query, values)
            self.db.commit()

        except Exception as e:
            print("Error updating course:", e)
            self.db.rollback()
            return False

        return True

    def select_by_id(self, course_id: int) -> Course:
        try:
            query = "SELECT * FROM course WHERE id = %s"
            values = (course_id,)

            cursor = self.db.cursor()
            cursor.execute(query, values)
            course_data = cursor.fetchone()

            if course_data:
                course = Course(*course_data)
                return course
            else:
                return None
        except Exception as e:
            print("Error selecting course by ID:", e)
            return None
