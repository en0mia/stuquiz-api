# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 05/07/23
import unittest
import uuid

from app.stuquiz.entities.admin import Admin


class TestAdmin(unittest.TestCase):
    TEST_ADMIN = Admin(str(uuid.uuid4()), 'username', 'test@test.com', 'password', 'salt')

    def testDump_returnCorrectDict(self):
        # Arrange
        expected_dict = {
            'id': self.TEST_ADMIN.id,
            'username': self.TEST_ADMIN.username,
            'email': self.TEST_ADMIN.email,
        }

        # Act
        result = self.TEST_ADMIN.dump()

        # Assert
        self.assertEqual(expected_dict, result)