'''
Test file for flask_app.py
Run with:
python -m unittest Tests/test_flask_app.py
'''

from flask_app import app
import unittest

class TestFlaskApp(unittest.TestCase):
    app = app.test_client() 

    def test_homepage(self):
        result = self.app.get('/',follow_redirects=True) 
        self.assertEqual(result.data, b"""Welcome to Emission Tracker!
    To view CO2 data from 2004 (or 1998/2018),
    enter the following: /year_co2/2004 \n
    To view the highest biofuel consumption for a country,
    enter the following: /biofuel/Canada""")

    def test_biofuel(self):
        result = self.app.get('/biofuel/Canada',follow_redirects=True) 
        self.assertEqual(result.data, b"Highest biofuel consumption for Canada is 3.192")
        result = self.app.get('/biofuel/Japan',follow_redirects=True) 
        self.assertEqual(result.data, b"Highest biofuel consumption for Japan is 9.034")

    def test_error(self):
        result = self.app.get('/Canada',follow_redirects=True) 
        self.assertEqual(result.data, b'Sorry, wrong format. Please enter one of the following commands: /year_co2/2004, /biofuel/Canada ')