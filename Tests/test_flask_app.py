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
        mock_average.return_value = '2.222'
        result = self.client.post("/average", 
                                  data = {'average_input': 'Canada'},
                                  follow_redirects=True)

        self.assertIn('2.222', result.data.decode('utf-8'))

        mock_average.assert_called_once_with("Canada")
