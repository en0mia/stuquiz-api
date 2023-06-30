# @author Lorenzo Varese
# @created 2023-06-30

import unittest
import uuid
from unittest.mock import MagicMock

from app.stuquiz.entities.category import Category
from app.stuquiz.entities.course import Course
from app.stuquiz.repositories.course_repository import CourseRepository


class TestCourseRepository(unittest.TestCase):
    TEST_ID = str(uuid.uuid4())

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

    def test_select_course_by_id(self):
        course_id = 123

        # Call the select_course_by_id method
        result = self.repository.select_course_by_id(course_id)

        # Assert that the select method was called with the correct query and argument
        expected_query = 'SELECT * FROM course WHERE id = %s'
        expected_arg = course_id
        self.cursor.execute.assert_called_once_with(expected_query, expected_arg)

        # Assert that the fetchone method was called to retrieve the selected course
        self.cursor.fetchone.assert_called_once()

        # Assert that the result is the expected Course instance or None if no course was found
        self.assertEqual(result, self.cursor.fetchone.return_value)
