# @author Lorenzo Varese
# @created 2023-06-30

import unittest
from unittest.mock import MagicMock

from app.stuquiz.entities.category import Category
from app.stuquiz.entities.course import Course
from app.stuquiz.repositories.course_repository import CourseRepository
from app.tests.repositories.test_constants import TEST_COURSE


class TestCourseRepository(unittest.TestCase):
    TEST_ID = TEST_COURSE.id
    test_course = TEST_COURSE

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

    def test_create_course(self):
        category = Category(
            id='category_id_1',
            name='Sample Category'
        )
        course = Course(
            id=self.TEST_ID,
            university_id='university_id_1',
            name='Sample Course',
            description='Sample Course Description',
            professor='Sample Professor',
            categories=[category],
            code='COURSE001'
        )

        # Call the create_course method
        result = self.repository.create_course(course)

        # Assert that the insert method was called with the correct query and arguments
        expected_query = 'INSERT INTO course (name, description, professor, code, university_id) ' \
                         'VALUES (%s, %s, %s, %s, %s)'
        expected_args = (course.name, course.description, course.professor, course.code, course.university_id)
        self.cursor.execute.assert_called_once_with(expected_query, expected_args)

        # Assert that the commit method was called on the database connection
        self.db.commit.assert_called_once()

        # Assert that the result is True, indicating successful creation
        self.assertTrue(result)

    def test_delete_course(self):
        course = Course(
            id=self.TEST_ID,
            university_id='university_id_1',
            name='Sample Course',
            description='Sample Course Description',
            professor='Sample Professor',
            categories=[],
            code='COURSE001'
        )

        # Call the delete_course method
        result = self.repository.delete_course(course)

        # Assert that the delete method was called with the correct query and argument
        expected_query = 'DELETE FROM course WHERE course_id = %s'
        expected_arg = course.id
        self.cursor.execute.assert_called_once_with(expected_query, expected_arg)

        # Assert that the commit method was called on the database connection
        self.db.commit.assert_called_once()

        # Assert that the result is True, indicating successful deletion
        self.assertTrue(result)

    def test_update_course(self):
        course = Course(
            id=self.TEST_ID,
            university_id='university_id_1',
            name='Sample Course',
            description='Sample Course Description',
            professor='Sample Professor',
            categories=[],
            code='COURSE001'
        )

        # Call the update_course method
        result = self.repository.update_course(course)

        # Assert that the update method was called with the correct query and arguments
        expected_query = 'UPDATE course SET name = %s, description = %s, professor = %s, ' \
                         'code = %s, university_id = %s WHERE id = %s'
        expected_args = (course.name, course.description, course.professor,
                         course.code, course.university_id, course.id)
        self.cursor.execute.assert_called_once_with(expected_query, expected_args)

        # Assert that the commit method was called on the database connection
        self.db.commit.assert_called_once()

        # Assert that the result is True, indicating successful update
        self.assertTrue(result)

    def test_select_course_by_id_when_course_exists(self):
        # Arrange
        expected_result = Course(self.test_course.id, self.test_course.university_id,
                                 self.test_course.name, self.test_course.description,
                                 self.test_course.professor, self.test_course.categories,
                                 self.test_course.code)

        self.cursor.fetchall.return_value = [(self.test_course.id, self.test_course.university_id,
                                              self.test_course.name, self.test_course.description,
                                              self.test_course.professor, self.test_course.categories,
                                              self.test_course.code)]

        # Act
        result = self.repository.select_course_by_id(self.test_course.id)

        # Assert
        self.assertEqual(expected_result, result)

    def test_select_course_by_id_when_course_doesnt_exist(self):
        # Arrange
        self.cursor.fetchall.return_value = None

        # Act
        result = self.repository.select_course_by_id(self.TEST_ID)

        # Assert
        self.assertIsNone(result)
