'''
Test file for flask_app.py
Run with:
python -m unittest flask_tests.py
'''

from flask_app import *
import unittest

class TestFlaskApp(unittest.TestCase):
    def test_route(self,route,output):
        self.app = app.test_client() 
        response = self.app.get(route, follow_redirects=True) 
        self.assertEqual(output, response.data) 

    def test_homepage(self):
        self.test_route('/',b'Hello')

    def test_biofuel(self):
        self.test_route('/biofuel',b'')