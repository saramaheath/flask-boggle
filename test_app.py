from unittest import TestCase

import json

from app import app, games

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class BoggleAppTestCase(TestCase):
    """Test flask app of Boggle."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Make sure information is in the session and HTML is displayed"""

        with self.client as client:
            response = client.get('/')
            ...
            # test that you're getting a template
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('<!-- html test -->', html)

    def test_api_new_game(self):
        """Test starting a new game.
        Checking if the route returns json with a string game
        id"""

        with self.client as client:
            response = client.post('/api/new-game')
            html = response.get_data(as_text=True)
            dict_response = json.loads(html)
            # breakpoint()
            # html = response.content_type(as_text=True)

            # testhi = "hello"
            # print(testhi)

            # write a test for this route
            self.assertIn("gameId",html)
            self.assertEqual(list,type(dict_response["board"][0]))
