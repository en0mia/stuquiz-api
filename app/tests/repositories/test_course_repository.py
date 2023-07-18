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
    test_category = None
    test_course = None

    def setUp(self) -> None:
        self.cursor = MagicMock()
        self.db = MagicMock()
        self.db_provider = MagicMock()

        self.db.cursor.return_value = self.cursor
        self.db_provider.get_db.return_value = self.db
        self.repository = CourseRepository(self.db_provider)

        self.test_category = Category(
            id=str(uuid.uuid4()),
            name="Test category"
        )

        self.test_course = Course(
            id=str(uuid.uuid4()),
            university_id=str(uuid.uuid4()),
            name="Test course",
            description="Test course description",
            professor="Test professor",
            categories=[self.test_category],
            code="TEST123"
        )

    def tearDown(self) -> None:
        self.cursor = None
        self.db = None
        self.db_provider = None
        self.repository = None
        self.test_category = None
        self.test_course = None

    def test_create_course(self):
        # Arrange
        expected_query = 'INSERT INTO course (name, description, professor, code, university_id) ' \
                         'VALUES (%s, %s, %s, %s, %s)'
        expected_args = (self.test_course.name, self.test_course.description, self.test_course.professor,
                         self.test_course.code, self.test_course.university_id)

        # Act
        result = self.repository.create_course(self.test_course)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_args)

        self.db.commit.assert_called_once()

        self.assertTrue(result)

    def test_delete_course(self):
        # Arrange
        expected_query = 'DELETE FROM course WHERE course_id = %s'
        expected_arg = (self.test_course.id,)

        # Act
        result = self.repository.delete_course(self.test_course)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_arg)

        self.db.commit.assert_called_once()

        self.assertTrue(result)

    def test_update_course(self):
        # Arrange
        expected_query = 'UPDATE course SET name = %s, description = %s, professor = %s, ' \
                         'code = %s, university_id = %s WHERE id = %s'
        expected_args = (self.test_course.name, self.test_course.description, self.test_course.professor,
                         self.test_course.code, self.test_course.university_id, self.test_course.id)

        # Act
        result = self.repository.update_course(self.test_course)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_args)

        self.db.commit.assert_called_once()

        self.assertTrue(result)

    def test_select_course_by_id_when_course_exists(self):
        # Arrange
        expected_result = Course(self.test_course.id, self.test_course.university_id,
                                 self.test_course.name, self.test_course.description,
                                 self.test_course.professor, self.test_course.code, self.test_course.categories)
        category = (self.test_category.id, self.test_category.name)
        expected_query = 'SELECT id, university_id, name, description, professor, code FROM course WHERE id = %s'
        expected_arg = (self.test_course.id, )
        self.cursor.fetchall.side_effect = [[(self.test_course.id, self.test_course.university_id,
                                             self.test_course.name, self.test_course.description,
                                             self.test_course.professor, self.test_course.code)], [category]]

        # Act
        result = self.repository.select_course_by_id(self.test_course.id)

        # Assert
        self.cursor.execute.assert_has_calls([mock.call(expected_query, expected_arg)])
        self.assertEqual(expected_result, result)

    def test_select_course_by_id_when_course_doesnt_exist(self):
        # Arrange
        self.cursor.fetchall.return_value = None

        # Act
        result = self.repository.select_course_by_id("test-id-00")

        # Assert
        self.assertIsNone(result)

    def test_selectCourseCategories_returnCategories_whenCategoriesExist(self):
        # Arrange
        first_category = (str(uuid.uuid4()), 'First category')
        second_category = (str(uuid.uuid4()), 'Second category')
        self.cursor.fetchall.return_value = [first_category, second_category]
        expected_result = [Category(*first_category), Category(*second_category)]
        expected_query = 'SELECT category.id, category.name FROM category, course, course_category ' \
                         'WHERE category.id = course_category.category_id ' \
                         'AND course.id = course_category.course_id AND course.id = %s'
        expected_arg = (self.test_course.id,)

        # Act
        result = self.repository.select_course_categories(self.test_course.id)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_arg)
        self.assertEqual(expected_result, result)

    def test_selectCourseCategories_returnEmptyList_whenCategoriesDontExist(self):
        # Arrange
        self.cursor.fetchall.return_value = None
        expected_result = []
        expected_query = 'SELECT category.id, category.name FROM category, course, course_category ' \
                         'WHERE category.id = course_category.category_id ' \
                         'AND course.id = course_category.course_id AND course.id = %s'
        expected_arg = (self.test_course.id, )

        # Act
        result = self.repository.select_course_categories(self.test_course.id)

        # Assert
        self.cursor.execute.assert_called_once_with(expected_query, expected_arg)
        self.assertEqual(expected_result, result)
