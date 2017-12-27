import unittest
from .. import app


class TestMain(unittest.TestCase):
    def setUp(self):
        # Init app
        app.testing = True
        self.app = app.test_client()

    def test_page(self):
        res = self.app.get('/test')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data.decode(), '<h1>Hello World</h1>')
