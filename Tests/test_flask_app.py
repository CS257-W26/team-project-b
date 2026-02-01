'''
Test file for flask_app.py
Run with:
python -m unittest flask_app.py
'''

from flask_app import *
import unittest

class TestFlaskApp(unittest.TestCase):
    app = app.test_client() 

    def test_homepage(self):
        result = self.app.get('/', follow_redirects=True) 
        self.assertEqual(result.data, b'Hello')

    def test_biofuel(self):
        result = self.app.get('/biofuel/Canada', follow_redirects=True) 
        self.assertEqual(result.data, b'Hello')

    def test_error(self):
        result = self.app.get('/Canada', follow_redirects=True) 
        self.assertEqual(result.data, b'Hello')