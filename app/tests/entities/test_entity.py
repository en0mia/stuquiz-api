# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 27/05/23
import unittest

from app.stuquiz.entities.university import University


class TestEntity(unittest.TestCase):
    TEST_ID = 1
    TEST_UUID = 'whatever UUID'
    TEST_NAME = 'whatever name'

    def test_dump(self):
        # Arrange
        input_args = (self.TEST_ID, self.TEST_UUID, self.TEST_NAME)
        expected_dict = {
            'id': self.TEST_ID,
            'uuid': self.TEST_UUID,
            'name': self.TEST_NAME
        }

        # Act
        university = University(*input_args)
        output = university.dump()

        # Assert
        self.assertEqual(expected_dict, output)
