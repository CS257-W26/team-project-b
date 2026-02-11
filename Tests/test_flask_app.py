'''
Test file for flask_app.py
Run with:
python -m unittest Tests/test_flask_app.py
'''
import unittest
from flask_app import app

class TestFlaskApp(unittest.TestCase):
    '''Purpose: Tests the route functions in flask_app'''
    app = app.test_client()

    def test_homepage(self):
        '''Argument: self
        Return: None
        Purpose: Tests home page for expected instructions
        '''
        result = self.app.get('/',follow_redirects=True)
        self.assertEqual(result.data, b'Welcome to Emission Tracker!\
    To view CO2 data from 2004 (or 1998/2018),\
    enter the following: /year_co2/2004 \n\
    To view the highest biofuel consumption for a country,\
    enter the following: /biofuel/Canada')

    def test_route_average(self):
        '''Argument: self
        Return: None
        Purpose: Tests average route for appropriate output messages
        '''
        dictionary = {'/average/Canada':b'The average annual CO2 emissions '
                      +'(measured in million tonnes) for Canada: 2.2296666666666667',
                      '/average/Japan':b'The average annual CO2 emissions '
                      +'(measured in million tonnes) for Japan: 3.6530000000000005'}
        for case,output in dictionary.items():
            result = self.app.get(case,follow_redirects=True)
            self.assertEqual(result.data, output)

    def test_route_ratio(self):
        '''Argument: self
        Return: None
        Purpose: Tests ratio route for expected output messages
        '''
        dictionary = {'/ratio/Canada':b'The ratio between averages of annual CO2 per capita '
                      +'(tonnes per person) to energy use per capita (kilowatt-hours per person) '
                      +'for Canada: 0.46071556778748357',
                      '/ratio/Japan':b'The ratio between averages of annual CO2 per capita '
                      +'(tonnes per person) to energy use per capita (kilowatt-hours per person) '
                      +'for Japan: 0.5552153473059571'}
        for case,output in dictionary.items():
            result = self.app.get(case,follow_redirects=True)
            self.assertEqual(result.data, output)

    def test_route_year_co2(self):
        '''Argument: self
        Return: None
        Purpose: Tests year_co2 route for expected output messages
        '''
        dictionary = {'/year_co2/2004':b'Annual CO2 emissions (measured in million tonnes) '
                      +'in the year 2004: Canada: 1.452\nJapan: 1.133\nArgentina: 0.630\n',
                    '/year_co2/2018':b'Annual CO2 emissions (measured in million tonnes) '
                    +'in the year 2018: Canada: 3.192\nJapan: 9.034\n'}
        for case,output in dictionary.items():
            result = self.app.get(case,follow_redirects=True)
            self.assertEqual(result.data, output)

    def test_route_biofuel(self):
        '''Argument: self
        Return: None
        Purpose: Tests biofuel route for expected output messages 
        '''
        dictionary = {'/biofuel/Canada':b'Highest biofuel consumption (measured in terawatt-hours) '
                      +'for Canada is 3.192',
                      '/biofuel/Japan':b'Highest biofuel consumption (measured in terawatt-hours) '
                      +'for Japan is 9.034'}
        for case,output in dictionary.items():
            result = self.app.get(case,follow_redirects=True)
            self.assertEqual(result.data, output)

    def test_error(self):
        '''Argument: self
        Return: None
        Purpose: Tests for error handling when wrong format is entered.
        '''
        dictionary = {'/Canada':b'Enter one of the following commands: /year_co2/2004, /biofuel/Canada'}
        for case,output in dictionary.items():
            result = self.app.get(case,follow_redirects=True)
            self.assertEqual(result.data, output)
