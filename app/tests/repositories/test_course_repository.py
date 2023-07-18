# @author Lorenzo Varese
# @created 2023-06-30

import unittest
import uuid
from unittest import mock
from unittest.mock import MagicMock

from app.stuquiz.entities.category import Category
from app.stuquiz.entities.course import Course
from app.stuquiz.repositories.course_repository import CourseRepository


class TestCourseRepository(unittest.TestCase):
    TEST_CATEGORY = Category(str(uuid.uuid4()), "Test category")
    TEST_COURSE = Course(str(uuid.uuid4()), str(uuid.uuid4()), "Test course", "Test course description",
                         "Test professor", "TEST123", [TEST_CATEGORY])

    def setUp(self) -> None:
        self.cursor = MagicMock()
        self.db = MagicMock()
        self.db_provider = MagicMock()
        self.db.cursor.return_value = self.cursor
        self.db_provider.get_db.return_value = self.db
        self.repository = CourseRepository(self.db_provider)

    def tearDown(self) -> None:
        self.cursor = None
        self.db = None
        self.db_provider = None
        self.repository = None

    def testCreateCourse_ReturnTrue_WhenCourseCreated(self):
        # Arrange
        expected_query = 'INSERT INTO course (name, description, professor, code, university_id) ' \
                         'VALUES (%s, %s, %s, %s, %s)'
        expected_args = (self.TEST_COURSE.name, self.TEST_COURSE.description, self.TEST_COURSE.professor,
                         self.TEST_COURSE.code, self.TEST_COURSE.university_id)

        # Act
        result = self.repository.create_course(self.TEST_COURSE)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_args)
        self.db.commit.assert_called_once()
        self.assertTrue(result)

    def testDeleteCourse_ReturnTrue_WhenCourseDeleted(self):
        # Arrange
        expected_query = 'DELETE FROM course WHERE course_id = %s'
        expected_arg = (self.TEST_COURSE.id,)

        # Act
        result = self.repository.delete_course(self.TEST_COURSE)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_arg)
        self.db.commit.assert_called_once()
        self.assertTrue(result)

    def testUpdateCourse_ReturnTrue_WhenCourseUpdated(self):
        # Arrange
        expected_query = 'UPDATE course SET name = %s, description = %s, professor = %s, ' \
                         'code = %s, university_id = %s WHERE id = %s'
        expected_args = (self.TEST_COURSE.name, self.TEST_COURSE.description, self.TEST_COURSE.professor,
                         self.TEST_COURSE.code, self.TEST_COURSE.university_id, self.TEST_COURSE.id)

        # Act
        result = self.repository.update_course(self.TEST_COURSE)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_args)
        self.db.commit.assert_called_once()
        self.assertTrue(result)

    def testSelectCourseById_ReturnCourse_WhenCourseExist(self):
        # Arrange
        expected_result = Course(self.TEST_COURSE.id, self.TEST_COURSE.university_id,
                                 self.TEST_COURSE.name, self.TEST_COURSE.description,
                                 self.TEST_COURSE.professor, self.TEST_COURSE.categories,
                                 self.TEST_COURSE.code)

        self.cursor.fetchall.return_value = [(self.TEST_COURSE.id, self.TEST_COURSE.university_id,
                                              self.TEST_COURSE.name, self.TEST_COURSE.description,
                                              self.TEST_COURSE.professor, self.TEST_COURSE.categories,
                                              self.TEST_COURSE.code)]

        # Act
        result = self.repository.select_course_by_id(self.TEST_COURSE.id)

        # Assert
        self.assertEqual(expected_result, result)

    def testSelectCourseById_ReturnNone_WhenCourseDontExist(self):
        # Arrange
        self.cursor.fetchall.return_value = None

        # Act
        result = self.repository.select_course_by_id("test-id-00")

        # Assert
        self.assertIsNone(result)

    def test_selectCoursesByUniversityID_returnCourses_whenCoursesExist(self):
        # Arrange
        first_course = (self.TEST_COURSE.id, self.TEST_COURSE.university_id, self.TEST_COURSE.name,
                        self.TEST_COURSE.description, self.TEST_COURSE.professor, self.TEST_COURSE.code)
        second_course = (str(uuid.uuid4()), self.TEST_COURSE.university_id, "name", "description", "professor",
                         "code")
        self.cursor.fetchall.side_effect = [[first_course, second_course], [], []]
        expected_result = [Course(*first_course), Course(*second_course)]
        expected_query = 'SELECT id, university_id, name, description, professor, code FROM course WHERE ' \
                         'university_id = %s'

        # Act
        result = self.repository.select_courses_by_university_id('university_id')

        # Assert
        self.cursor.execute.assert_has_calls([mock.call(expected_query, ('university_id',))])
        self.assertEqual(expected_result, result)

    def test_selectCoursesByUniversityID_returnEmptyList_whenCoursesDontExist(self):
        # Arrange
        self.cursor.fetchall.return_value = None
        expected_result = []
        expected_query = 'SELECT id, university_id, name, description, professor, code FROM course WHERE ' \
                         'university_id = %s'

        # Act
        result = self.repository.select_courses_by_university_id('university_id')

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, ('university_id',))
        self.assertEqual(expected_result, result)

    def test_selectCourseCategories_returnCategories_whenCategoriesExist(self):
        # Arrange
        first_category = (str(uuid.uuid4()), 'First category')
        second_category = (str(uuid.uuid4()), 'Second category')
        self.cursor.fetchall.return_value = [first_category, second_category]
        expected_result = [Category(*first_category), Category(*second_category)]
        expected_query = 'SELECT category.id, category.name FROM category, course, course_category ' \
                'WHERE category.id = course_category.category_id ' \
                'AND course.id = course_category.course_id AND course.id = %s'

        # Act
        result = self.repository.select_course_categories('course_id')

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, ('course_id',))
        self.assertEqual(expected_result, result)

    def test_selectCourseCategories_returnEmptyList_whenCategoriesDontExist(self):
        # Arrange
        self.cursor.fetchall.return_value = None
        expected_result = []
        expected_query = 'SELECT category.id, category.name FROM category, course, course_category ' \
                         'WHERE category.id = course_category.category_id ' \
                         'AND course.id = course_category.course_id AND course.id = %s'

        # Act
        result = self.repository.select_course_categories('course_id')

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, ('course_id',))
        self.assertEqual(expected_result, result)
