# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 22/05/23
import unittest
from app import stuquiz


class Hello(unittest.TestCase):

    def setUp(self):
        app = stuquiz.create_app()
        app.testing = True
        self.app = app.test_client()

    def test_home(self):
        result = self.app.get('/hello')
        self.assertEqual(result.status_code, 200)
