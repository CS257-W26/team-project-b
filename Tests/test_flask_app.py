'''
Test file for flask_app.py
'''
import unittest
from unittest.mock import patch
from flask_app import app

class TestFlaskApp(unittest.TestCase) :
    '''Purpose: Tests the user front facing website'''

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    @patch('flask_app.route_api_average')
    @patch('flask_app.route_api_ratio')
    @patch('flask_app.route_api_biofuel')
    def test_route_country_stats(self, mock_average, mock_ratio, mock_biofuel):
        '''Argument: self, mock_average
        Return: None
        Purpose: Tests stat route for appropriate output messages
        '''
        mock_average.return_value = '5.5'
        mock_ratio.return_value = '2.3'
        mock_biofuel.return_value = '1.1'
        result = self.client.get('/stats', query_string= {'country_stats': 'Canada'})

        self.assertIn('5.5', result.data.decode('utf-8'))
        self.assertIn('Canada', result.data.decode('utf-8'))

        mock_average.assert_called_once_with('Canada')
        mock_ratio.assert_called_once_with('Canada')
        mock_biofuel.assert_called_once_with('Canada')

    @patch('flask_app.route_api_year_co2')
    def test_route_year_co2(self, mock_year_co2):
        '''Argument: self, mock_year_co2
        Return: None
        Purpose: Tests year_co2 route for appropriate output
        '''
        result = self.client.get('/year_co2', query_string = {'year_co2': 2000})

        self.assertIn('2000', result.data.decode('utf-8'))
        mock_year_co2.assert_called_once_with('2000')

    @patch('flask_app.route_api_year_energy')
    def test_route_year_energy(self, mock_year_energy):
        '''Argument: self, mock_year_energy
        Return: None
        Purpose: Tests year_energy route for appropriate output
        '''
        result = self.client.get('/year_energy', query_string = {'year_energy': 2000})
        self.assertIn('2000', result.data.decode('utf-8'))
        mock_year_energy.assert_called_once_with('2000')

    def test_route_graph(self):
        '''Argument: self
        Return: None
        Purpose: Tests year_energy route for appropriate output
        '''
        result = self.client.get('/graph', query_string = {'graph_country': "Canada"})
        self.assertIn('Graph', result.data.decode('utf-8'))
