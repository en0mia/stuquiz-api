# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 20/07/23
import json
import unittest
import uuid
from unittest.mock import MagicMock

from app.stuquiz.controllers.course.update_course_controller import UpdateCourseController
from app.stuquiz.entities.course import Course
from app.stuquiz.entities.university import University
from app.tests.controllers.course.course_controllers_utils import CourseControllersUtils


class TestUpdateCourseController(unittest.TestCase):
    TEST_UNIVERSITY = University(str(uuid.uuid4()), 'Name')

    @staticmethod
    def course_to_dict(course: Course) -> dict:
        """Returns a dict representation of the course.
        This method differs from Course.dump() since the Course's ID is associated to the key course_id
        instead of id.
        :param course: Course
        :return: dict
        """
        return {
            'course_id': course.id,
            'university_id': course.university_id,
            'name': course.name,
            'description': course.description,
            'professor_id': course.professor_id,
            'code': course.code
        }

    def setUp(self) -> None:
        self.course_model = MagicMock()
        self.admin_model = MagicMock()
        self.university_model = MagicMock()
        self.controller = UpdateCourseController(self.course_model, self.admin_model, self.university_model)

    def tearDown(self) -> None:
        self.course_model = None
        self.admin_model = None
        self.university_model = None
        self.controller = None

    def testExecute_return401_whenAdminNotLoggedIn(self):
        # Arrange
        course = CourseControllersUtils.generate_courses(1)
        self.admin_model.is_admin_logged_in.return_value = False

        # Act
        result = self.controller.execute(course[0].dump())

        # Assert
        self.admin_model.is_admin_logged_in.assert_called_once()
        self.course_model.update_course.assert_not_called()
        self.assertEqual(401, result.status_code)

    def testExecute_return400_whenInvalidParameters(self):
        # Arrange
        self.admin_model.is_admin_logged_in.return_value = True

        # Act
        result = self.controller.execute({
            'university_id': 'invalid id',
            'name': None,
            'description': None,
            'professor_id': 'invalid id',
            'code': None
        })

        # Assert
        self.admin_model.is_admin_logged_in.assert_called_once()
        self.course_model.update_course.assert_not_called()
        self.assertEqual(400, result.status_code)

    def testExecute_return404_whenCourseDontExist(self):
        # Arrange
        course = CourseControllersUtils.generate_courses(1)
        self.admin_model.is_admin_logged_in.return_value = True
        self.course_model.get_course_by_id.return_value = None

        # Act
        result = self.controller.execute(self.course_to_dict(course[0]))

        # Assert
        self.admin_model.is_admin_logged_in.assert_called_once()
        self.course_model.get_course_by_id.assert_called_once()
        self.course_model.update_course.assert_not_called()
        self.assertEqual(404, result.status_code)

    def testExecute_return400_whenUniversityDontExist(self):
        # Arrange
        course = CourseControllersUtils.generate_courses(1)
        self.admin_model.is_admin_logged_in.return_value = True
        self.course_model.get_course_by_id.return_value = course[0]
        self.university_model.get_university_by_id.return_value = None

        # Act
        result = self.controller.execute(self.course_to_dict(course[0]))

        # Assert
        self.admin_model.is_admin_logged_in.assert_called_once()
        self.university_model.get_university_by_id.assert_called_once()
        self.course_model.update_course.assert_not_called()
        self.assertEqual(400, result.status_code)

    def testExecute_return500_whenDbError(self):
        # Arrange
        course = CourseControllersUtils.generate_courses(1)
        self.admin_model.is_admin_logged_in.return_value = True
        self.course_model.update_course.return_value = False
        self.course_model.get_course_by_id.return_value = course[0]
        self.university_model.get_university_by_id.return_value = self.TEST_UNIVERSITY

        # Act
        result = self.controller.execute(self.course_to_dict(course[0]))

        # Assert
        self.admin_model.is_admin_logged_in.assert_called_once()
        self.university_model.get_university_by_id.assert_called_once()
        self.course_model.update_course.assert_called_once()
        self.assertEqual(500, result.status_code)

    def testExecute_return200WithEmptyBody_whenCourseHasBeenUpdated(self):
        # Arrange
        course = CourseControllersUtils.generate_courses(1)
        expected_body = {}
        self.course_model.update_course.return_value = True
        self.admin_model.is_admin_logged_in.return_value = True
        self.university_model.get_university_by_id.return_value = self.TEST_UNIVERSITY

        # Act
        result = self.controller.execute(self.course_to_dict(course[0]))

        # Assert
        self.admin_model.is_admin_logged_in.assert_called_once()
        self.course_model.update_course.assert_called_once()
        self.university_model.get_university_by_id.assert_called_once()
        self.assertEqual(200, result.status_code)
        self.assertEqual(expected_body, json.loads(result.data))
