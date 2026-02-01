'''modules for testing basic_cl.py main function'''
import sys
import unittest
from io import StringIO
from ProductionCode.core import Features

class TestCommandLine(unittest.TestCase):
    '''Arguments: unittest.TestCase
    Return value: none
    Purpose: Holds the tests for command_line.py
    '''
    
    core = Features()

    def test_average(self):
        '''Arguments: self (TestCommandLine)
        Return: none
        Purpose: Tests the average_co2 function in command_line.py
        '''
        self.assertAlmostEqual(self.core.average('Canada','Data/dummy_data.csv',2),2.22966667)
        self.assertAlmostEqual(self.core.average('Japan','Data/dummy_data.csv',2),3.65300)
        self.assertAlmostEqual(self.core.average('Argentina','Data/dummy_energy_data.csv',2),1.27366667)

    def test_average_edge(self):
        '''Arguments: self (TestCommandLine)
        Return: none
        Purpose: Tests edge cases for the average_co2 function in command_line.py
        '''
        self.assertEqual(self.core.average(12,'Data/dummy_data.csv',2), 'Please input a string for a country')
        self.assertEqual(self.core.average('','Data/dummy_data.csv',2), 'Please input a valid country')

    def test_ratio(self):
        '''Arguments: self (TestCommandLine)
        Return: none
        Purpose: Tests the ratio function in command_line.py
        '''
        self.assertAlmostEqual(self.core.ratio('Canada'),0.460715567)
        self.assertAlmostEqual(self.core.ratio('Japan'),0.555215345)

    def test_year_co2(self):
        '''Arguments: self (TestCommandLine)
        Return: none
        Purpose: Tests year_co2 function in command_line.py
        '''
        self.assertEqual(self.core.year_co2('2004'),[['Canada','2004','1.452'],
        ['Japan','2004','1.133'],['Argentina','2004','0.630']])

        self.assertEqual(self.core.year_co2('1998'),[['Canada','1998','2.045'],
        ['Japan','1998','0.792'],['Argentina','1998','1.582']])

    def test_year_co2_edge(self):
        '''Arguments: self (TestCommandLine)
        Return: none
        Purpose: Tests edge cases for the year_co2 function in command_line.py
        '''
        self.assertEqual(self.core.year_co2(2004), "Please input a valid year")
        self.assertEqual(self.core.year_co2("Canadaa"), "Please input a valid year")

    def test_biofuel_consumption(self):
        '''Arguments: self (TestCommandLine)
        Return: none
        Purpose: Tests highest_co2 function in command_line.py
        '''
        self.assertEqual(self.core.highest_biofuel_consumption("Canada"),3.192)
        self.assertEqual(self.core.highest_biofuel_consumption("Japan"),9.034)

    def test_biofuel_consumption_edge(self):
        '''Arguments: self (TestCommandLine)
        Return: none
        Purpose: Tests edge cases for highest_co2 function in command_line.py
        '''
        self.assertEqual(self.core.highest_biofuel_consumption(123), "Invalid input")
