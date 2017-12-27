import unittest
from .. import app, get_tweets


class TestMain(unittest.TestCase):
    def setUp(self):
        # Init app
        app.testing = True
        self.app = app.test_client()

    def test_page(self):
        # Make sure test page runs normally
        res = self.app.get('/test')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data.decode(), '<h1>Hello World</h1>')

    def test_secure_keys(self):
        # Make sure all env variables are set properly
        self.assertEqual(app.config['TEST'], 'VALUE')

    def test_tweets(self):
        # Make sure we can connect to API
        res = get_tweets(app.config['DEFAULT_TWITTER_USERNAME'])
        self.assertIsNotNone(res)

    def test_load_page(self):
        # Make sure HTML renders properly
        res = self.app.get(app.config['TWEET_PATH'] + app.config['DEFAULT_TWITTER_USERNAME'])
        html = res.data.decode()
        self.assertIsNotNone(html)
        self.assertGreater(html.find(app.config['DEFAULT_TWITTER_USERNAME']), -1)

    def test_load_bad_username(self):
        # Make sure bad username does not work
        res = self.app.get(app.config['TWEET_PATH'] + app.config['BAD_TWITTER_USERNAME'])
        html = res.data.decode()
        self.assertIsNotNone(html)
        self.assertEqual(html.find('small'), -1)
