'''
Test file for flask_app.py
'''
import unittest
from unittest.mock import patch
from flask_app import app, api

class TestFlaskApp(unittest.TestCase) :
    '''Purpose: Tests the user front facing website'''

    @patch('flask_app.api.route_average')
    def test_route_average(self, mock_average):
        '''Argument: self, mock_average
        Return: None
        Purpose: Tests average route for appropriate output messages
        '''
        mock_average.return_value = 2.222
        result = self.client.get("/average/Canada", follow_redirects=True)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data.decode('utf-8'), '2.222')

        mock_average.assert_called_once_with("Canada")
