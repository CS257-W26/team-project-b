'''
Test file for flask_app.py
Run with:
python -m unittest flask_app.py
'''

from flask_app import *
import unittest

class TestFlaskApp(unittest.TestCase):
    def test_route(self,route):
        self.app = app.test_client() 
        return self.app.get(route, follow_redirects=True) 
        

    def test_homepage(self):
        self.assertEqual(self.test_route('/'), b'Hello') 

    def test_biofuel(self):
        self.assertEqual(self.test_route('/biofuel/Canada'), b'Hello')

    def test_error(self):
        self.assertEqual(self.test_route('/Canada'), b'Sorry, wrong format - ') 