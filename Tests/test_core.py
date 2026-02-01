'''modules for testing basic_cl.py main function'''
import sys
import unittest
from io import StringIO
from ProductionCode.core import Features

class TestCommandLine(unittest.TestCase):
    '''Arguments: unittest.TestCase
    Return value: none
    Purpose: Holds the tests for command_line.py
    Run with: python -m unittest Tests/test_core.py
    '''
    
    core = Features()

    def test_average(self):
        '''Arguments: self (TestCommandLine)
        Return: none
        Purpose: Tests the average_co2 function in command_line.py
        '''
        self.assertAlmostEqual(self.core.average([12.345,10.432,15.725]),2.22966667)
        self.assertAlmostEqual(self.core.average([12.333,8.324,20.324]),3.65300)
        self.assertAlmostEqual(self.core.average([1.234,9.87,10.23]),1.27366667)

    def test_average_edge(self):
        '''Arguments: self (TestCommandLine)
        Return: none
        Purpose: Tests edge cases for the average_co2 function in command_line.py
        '''
        self.assertEqual(self.core.average(['Hello','Goodbye']), 'No data found')
        self.assertEqual(self.core.average([]), 'No data found')

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
        self.assertEqual(self.core.year_co2(2004), [])
        self.assertEqual(self.core.year_co2("Canadaa"), [])

    def test_highest_biofuel(self):
        '''Arguments: self (TestCommandLine)
        Return: none
        Purpose: Tests highest_co2 function in command_line.py
        '''
        self.assertEqual(self.core.highest_biofuel("Canada"),3.192)
        self.assertEqual(self.core.highest_biofuel("Japan"),9.034)

    def test_biofuel_edge(self):
        '''Arguments: self (TestCommandLine)
        Return: none
        Purpose: Tests edge cases for highest_co2 function in command_line.py
        '''
        self.assertEqual(self.core.highest_biofuel(123), "Invalid input")
