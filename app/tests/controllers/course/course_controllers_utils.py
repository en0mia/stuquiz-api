# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 19/07/23
import uuid

from app.stuquiz.entities.category import Category
from app.stuquiz.entities.course import Course


class CourseControllersUtils(object):
    @staticmethod
    def generate_expected_body(courses: list[Course]) -> list[dict]:
        return [{
            'id': course.id,
            'university_id': course.university_id,
            'name': course.name,
            'description': course.description,
            'professor_id': course.professor_id,
            'categories': [category.dump() for category in course.categories],
            'code': course.code
        } for course in courses]

    @staticmethod
    def generate_courses(number: int) -> list[Course]:
        return [Course(str(uuid.uuid4()), str(uuid.uuid4()), f"Test course %s" % i,
                       f"Test course %s description" % i, str(uuid.uuid4()), f"TEST%s" % i,
                       [Category(str(uuid.uuid4()), f"Test category %s" % i)]) for i in range(1, number + 1)]
