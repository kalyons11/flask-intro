import unittest
from .. import app, get_tweets


class TestMain(unittest.TestCase):
    def setUp(self):
        # Init app
        app.testing = True
        self.app = app.test_client()

    def test_page(self):
        res = self.app.get('/test')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data.decode(), '<h1>Hello World</h1>')

    def test_secure_keys(self):
        self.assertEqual(app.config['TEST'], 'VALUE')

    def test_tweets(self):
        pass
        # self.assertIsNone(app.config['TWITTER_ACCESS_TOKEN'])
        # res = get_tweets(app.config['DEFAULT_TWITTER_USERNAME'])
        # self.assertIsNotNone(res)
