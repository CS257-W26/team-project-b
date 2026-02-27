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
    def test_route_average(self, mock_average):
        '''Argument: self, mock_average
        Return: None
        Purpose: Tests average route for appropriate output messages
        '''
        mock_average.return_value = '5.5'
        
        result = self.client.get('/average', query_string= {'average_country': 'Canada'})

        self.assertIn('5.5', result.data.decode('utf-8'))
        self.assertIn('Canada', result.data.decode('utf-8'))

        mock_average.assert_called_once_with('Canada')

    @patch('flask_app.route_api_ratio')
    def test_route_ratio(self, mock_ratio):
        '''Argument: self, mock_ratio
        Return: None
        Purpose: Tests ratio route for appropriate output
        '''
        mock_ratio.return_value = '12.5'

        result = self.client.get('/ratio', query_string = {'ratio_country' : 'Canada'})

        self.assertIn('12.5', result.data.decode('utf-8'))
        self.assertIn('Canada', result.data.decode('utf-8'))

        mock_ratio.assert_called_once_with('Canada')

    @patch('flask_app.route_api_biofuel')
    def test_route_biofuel(self, mock_biofuel):
        '''Argument: self, mock_biofuel
        Return: None
        Purpose: Tests ratio route for appropriate output
        '''
        mock_biofuel.return_value = '11.1'

        result = self.client.get(
            '/biofuel', query_string = {'biofuel_country': 'Japan'}
        )

        self.assertIn('11.1', result.data.decode('utf-8'))
        self.assertIn('Japan', result.data.decode('utf-8'))

        mock_biofuel.assert_called_once_with('Japan')
        
        
