'''
Test file for flask_api.py
Run with:
python -m unittest Tests/test_flask_api.py
'''
import unittest
from unittest.mock import patch
from flask_api import app, api

class TestFlaskApi(unittest.TestCase):
    '''Purpose: Tests the api route functions in flask_app'''
    def setUp(self):
        if "api" not in app.blueprints:
            app.register_blueprint(api, url_prefix = "/api")
        self.client = app.test_client()
        self.client.testing = True

    def test_homepage(self):
        '''Argument: self
        Return: None
        Purpose: Tests home page for expected instructions
        '''
        result = self.client.get('/',follow_redirects=True)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data.decode('utf-8'), 'Welcome to Emission Tracker!\
    To view CO2 data from 2004 (or 1998/2018),\
    enter the following: /year_co2/2004 \n\
    To view the highest biofuel consumption for a country,\
    enter the following: /biofuel/Canada')

    @patch('flask_api.core.average')
    def test_route_average(self, mock_average):
        '''Argument: self, mock_average
        Return: None
        Purpose: Tests average route for appropriate output messages
        '''
        mock_average.return_value = 2.222
        result = self.client.get("/api/average/Canada", follow_redirects=True)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data.decode('utf-8'), '2.222')

        mock_average.assert_called_once_with("Canada")

    @patch('flask_api.core.ratio')
    def test_route_ratio(self, mock_ratio):
        '''Argument: self, mock_ratio
        Return: None
        Purpose: Tests ratio route for expected output messages
        '''
        mock_ratio.return_value = 1.24
        result = self.client.get("/api/ratio/Canada", follow_redirects = True)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data.decode('utf-8'),"1.24")
        mock_ratio.assert_called_once_with("Canada")

    @patch('flask_api.core.year_co2')
    def test_route_year_co2(self, mock_year_co2):
        '''Argument: self
        Return: None
        Purpose: Tests year_co2 route for expected output messages
        '''
        mock_year_co2.return_value = "['Canada','2000','2.3']"
        result = self.client.get("/api/year_co2/2000", follow_redirects = True)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data.decode('utf-8'),
                          "['Canada','2000','2.3']"
                        )
        mock_year_co2.assert_called_once_with("2000")

    @patch('flask_api.core.year_energy')
    def test_route_year_energy(self, mock_year_energy):
        '''Argument: self
        Return: None
        Purpose: Tests year_co2 route for expected output messages
        '''
        mock_year_energy.return_value = "['Canada','2000','2.3']"
        result = self.client.get("/api/year_energy/2000", follow_redirects = True)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data.decode('utf-8'),
                          "['Canada','2000','2.3']"
                        )
        mock_year_energy.assert_called_once_with("2000")

    @patch('flask_api.core.highest_biofuel')
    def test_route_biofuel(self, mock_biofuel):
        '''Argument: self
        Return: None
        Purpose: Tests biofuel route for expected output messages 
        '''
        mock_biofuel.return_value = 3.2
        result = self.client.get("/api/biofuel/Canada", follow_redirects = True)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data.decode('utf-8'),"3.2"
                        )

    def test_error(self):
        '''Argument: self
        Return: None
        Purpose: Tests for error handling when wrong format is entered.
        '''
        result = self.client.get("/Canaada",follow_redirects=True)
        self.assertEqual(result.status_code, 200)
        self.assertIn(" Try: /api/year_co2/2004, /api/biofuel/Canada",
                      result.data.decode('utf-8')
                     )
