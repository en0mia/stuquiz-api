# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 20/07/23
import json
import unittest
import uuid
from unittest import mock
from unittest.mock import MagicMock

from app.stuquiz.controllers.course.update_course_controller import UpdateCourseController
from app.stuquiz.entities.course import Course
from app.stuquiz.entities.university import University
from app.tests.controllers.course.course_controllers_utils import CourseControllersUtils


class TestUpdateCourseController(unittest.TestCase):
    TEST_UNIVERSITY = University(str(uuid.uuid4()), 'Name')
    TEST_COURSE = CourseControllersUtils.generate_courses(1)[0]

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
        self.request = MagicMock()
        self.course_model = MagicMock()
        self.admin_model = MagicMock()
        self.university_model = MagicMock()
        self.controller = UpdateCourseController(self.course_model, self.university_model)
        self.args = mock.PropertyMock(return_value={'course_id': str(uuid.uuid4())})
        self.form = mock.PropertyMock(return_value=self.course_to_dict(self.TEST_COURSE))
        type(self.request).args = self.args
        type(self.request).form = self.form

    def tearDown(self) -> None:
        self.request = None
        self.course_model = None
        self.admin_model = None
        self.university_model = None
        self.controller = None
        self.args = None
        self.form = None

    def testExecute_return404_whenCourseDontExist(self):
        # Arrange
        self.course_model.get_course_by_id.return_value = None

        # Act
        result = self.controller.execute(self.request)

        # Assert
        self.args.assert_called_once()
        self.assertEqual(5, self.form.call_count)
        self.course_model.get_course_by_id.assert_called_once()
        self.course_model.update_course.assert_not_called()
        self.assertEqual(404, result.status_code)

    def testExecute_return400_whenUniversityDontExist(self):
        # Arrange
        self.course_model.get_course_by_id.return_value = self.TEST_COURSE
        self.university_model.get_university_by_id.return_value = None

        # Act
        result = self.controller.execute(self.request)

        # Assert
        self.args.assert_called_once()
        self.assertEqual(5, self.form.call_count)
        self.university_model.get_university_by_id.assert_called_once()
        self.course_model.update_course.assert_not_called()
        self.assertEqual(400, result.status_code)

    def testExecute_return500_whenDbError(self):
        # Arrange
        self.course_model.update_course.return_value = False
        self.course_model.get_course_by_id.return_value = self.TEST_COURSE
        self.university_model.get_university_by_id.return_value = self.TEST_UNIVERSITY

        # Act
        result = self.controller.execute(self.request)

        # Assert
        self.args.assert_called_once()
        self.assertEqual(5, self.form.call_count)
        self.university_model.get_university_by_id.assert_called_once()
        self.course_model.update_course.assert_called_once()
        self.assertEqual(500, result.status_code)

    def testExecute_return200WithEmptyBody_whenCourseHasBeenUpdated(self):
        # Arrange
        expected_body = {}
        self.course_model.update_course.return_value = True
        self.university_model.get_university_by_id.return_value = self.TEST_UNIVERSITY

        # Act
        result = self.controller.execute(self.request)

        # Assert
        self.args.assert_called_once()
        self.assertEqual(5, self.form.call_count)
        self.course_model.update_course.assert_called_once()
        self.university_model.get_university_by_id.assert_called_once()
        self.assertEqual(200, result.status_code)
        self.assertEqual(expected_body, json.loads(result.data))
