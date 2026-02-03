'''modules for testing basic_cl.py main function'''
import unittest
from ProductionCode.core import Features
from ProductionCode.data_handling import DataHandler

class TestCommandLine(unittest.TestCase):
    '''Arguments: unittest.TestCase
    Return value: none
    Purpose: Holds the tests for core.py
    Run with: python -m unittest Tests/test_core.py
    '''

    core = Features()
    handler = DataHandler()

    data = handler.load_data("Data/dummy_data.csv")

    def test_average(self):
        '''Arguments: self (TestCommandLine)
        Return: none
        Purpose: Tests the average_co2 function in command_line.py
        '''
        #Average for Canada cumulative_co2
        self.assertAlmostEqual(float(self.core.average([1.452,2.045,3.192])),2.22966667)
        #Average for Canada co2_per_capita
        self.assertAlmostEqual(float(self.core.average([12.345,10.432,15.725])),12.83400)
        #Average for Japan co2_per_capita
        self.assertAlmostEqual(float(self.core.average([12.333,8.324,20.324])),13.6603333)
        #Average for Argetina co2_per_capita
        self.assertAlmostEqual(float(self.core.average([1.234,9.87,10.23])),7.11133333)

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
        self.assertAlmostEqual(self.core.ratio([12.345,10.432,15.725],
        [42.47,30.90,10.20]),0.460715567)
        self.assertAlmostEqual(self.core.ratio([12.333,8.324,20.324],
        [4.359,24.132,45.32]),0.555215345)

    def test_year_co2(self):
        '''Arguments: self (TestCommandLine)
        Return: none
        Purpose: Tests year_co2 function in command_line.py
        '''
        self.assertEqual(self.core.year_co2('2004', self.data),[['Canada','2004','1.452'],
        ['Japan','2004','1.133'],['Argentina','2004','0.630']])

        self.assertEqual(self.core.year_co2('1998', self.data),[['Canada','1998','2.045'],
        ['Japan','1998','0.792'],['Argentina','1998','1.582']])

    def test_year_co2_edge(self):
        '''Arguments: self (TestCommandLine)
        Return: none
        Purpose: Tests edge cases for the year_co2 function in command_line.py
        '''
        self.assertEqual(self.core.year_co2(2004, self.data), [])
        self.assertEqual(self.core.year_co2("Canadaa", self.data), [])

    def test_highest_biofuel(self):
        '''Arguments: self (TestCommandLine)
        Return: none
        Purpose: Tests highest_co2 function in command_line.py
        '''
        self.assertEqual(self.core.highest_biofuel([1.452,2.045,3.192]),3.192)
        self.assertEqual(self.core.highest_biofuel([1.133,0.792,9.034]),9.034)

    def test_biofuel_edge(self):
        '''Arguments: self (TestCommandLine)
        Return: none
        Purpose: Tests edge cases for highest_co2 function in command_line.py
        '''
        self.assertEqual(self.core.highest_biofuel(123), "Invalid input")
