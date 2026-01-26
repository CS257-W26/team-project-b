import unittest
from command_line import average,year_co2,highest_biofuel_consumption,load_data,main

class TestCommandLine(unittest.TestCase):
    maxDiff = None

    def test_load_data(self):
        '''Arguments: self (TestCommandLine)
        Return: none
        Purpose: Tests load data with the dummy_data.csv file
        '''
        
        self.assertEqual(load_data('Data/dummy_data_one_line.csv'),[['country', 'year', 'cumulative_co2']])
        self.assertEqual(load_data('Data/dummy_data.csv'), [['country', 'year', 'cumulative_co2'],['Canada', '2004', '1.452'],
        ['Canada', '1998', '2.045'],
        ['Canada', '2018','3.192'],
        ['Japan', '2004', '1.133'],
        ['Japan', '1998', '0.792'],
        ['Japan', '2018', '9.034'],
        ['Argentina', '2004', '0.630'],
        ['Argentina', '1998', '1.582'],
        ['Argentina', '2018', ''],
        ['Argentina', '2019', '1.609']])
    
    def test_average(self):
        '''Arguments: self (TestCommandLine)
        Return: none
        Purpose: Tests the average_co2 function in command_line.py
        '''
        self.assertAlmostEqual(average('Canada','Data/dummy_data.csv'),2.22966667)
        self.assertAlmostEqual(average('Japan','Data/dummy_data.csv'),3.65300)
        self.assertAlmostEqual(average('Argentina','Data/dummy_energy_data.csv'),1.27366667)

    def test_average_edge(self):
        '''Arguments: self (TestCommandLine)
        Return: none
        Purpose: Tests edge cases for the average_co2 function in command_line.py
        '''
        self.assertEqual(average(12,'Data/dummy_data.csv'), 'Please input a string for a country')
        self.assertEqual(average('','Data/dummy_data.csv'), 'Please input a valid country')

    def test_year_co2(self):
        '''Arguments: self (TestCommandLine)
        Return: none
        Purpose: Tests the year_co2 function in command_line.py
        '''
        self.assertEqual(year_co2('2004'), [['Canada', '2004', '1.452'], ['Japan', '2004', '1.133'], ['Argentina', '2004', '0.630']])
        self.assertEqual(year_co2('1998'), [['Canada', '1998', '2.045'], ['Japan', '1998', '0.792'], ['Argentina', '2004', '1.582']])

    def test_year_co2_edge(self):
        '''Arguments: self (TestCommandLine)
        Return: none
        Purpose: Tests edge cases for the year_co2 function in command_line.py
        '''
        self.assertEqual(year_co2(2004), "Please input a valid year")
        self.assertEqual(year_co2("Canadaa"), "Please input a valid year")

    def test_biofuel_consumption(self):
        '''Arguments: self (TestCommandLine)
        Return: none
        Purpose: Tests highest_co2 function in command_line.py
        '''
        self.assertEqual(highest_biofuel_consumption("Canada"), 3.192)
        self.assertEqual(highest_biofuel_consumption("Japan"), 9.034)

    def test_biofuel_consumption_edge(self):
        '''Arguments: self (TestCommandLine)
        Return: none
        Purpose: Tests edge cases for highest_co2 function in command_line.py
        '''
        self.assertEqual(highest_biofuel_consumption(1234), "Invalid input")