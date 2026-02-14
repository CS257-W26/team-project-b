'''modules for testing basic_cl.py main function'''
import sys
import unittest
from unittest.mock import patch
from io import StringIO
from command_line import main

class TestCommandLine(unittest.TestCase):
    '''Arguments: unittest.TestCase
    Return value: none
    Purpose: Holds the tests for command_line.py
    '''
    @patch ('command_line.co2_data',
           'Data/dummy_data.csv')
    @patch ('command_line.energy_data',
            'Data/dummy_energy_data.csv')
    @patch ('command_line.wanted_columns',
            [2,3])
    def sys_helper(self):
        '''Arguments: self
        Return value: Returns sys.stdout output (str)
        Purpose: Reduces duplicated code by returning output from sys.stdout
        '''
        sys.stdout = StringIO()
        main()
        return sys.stdout.getvalue().strip()

    @patch ('command_line.CO2_DATA',
            )
    def test_arg_ratio(self):
        '''Arguments: self (TestProductionCode)
        Return value: None
        Purpose: Tests whether the main function returns the correct value for the
        specified function in command line arguments
        '''
        sys.argv = ['command_line.py','--ratio','Canada']
        self.assertEqual(self.sys_helper(), "0.46071556778748357")

    def test_arg_average(self):
        '''Arguments: self (TestProductionCode)
        Return value: None
        Purpose: Tests main function's output for arg.average
        '''
        sys.argv = ['command_line.py', '--average', 'Japan']
        self.assertEqual(self.sys_helper(), '3.6530000000000005')

    def test_arg_biofuel(self):
        '''Arguments: self (TestProductionCode)
        Return value: None
        Purpose: Tests if biofuel argument in main works as expected
        '''
        sys.argv = ['command_line.py', '--biofuel', 'Canada']
        self.assertEqual(self.sys_helper(), '3.192')

    def test_arg_year_co2(self):
        '''Arguments: self (TestProductionCode)
        Return value: None
        Purpose: Tests if year_co2 argument in main displays correct output
        '''
        sys.argv = ['command_line.py', '--year_co2', '1998']
        self.assertEqual(self.sys_helper(), 
        'Annual CO2 emissions (measured in million tonnes) in the year 2019: Argentina: 1.609')

    def test_no_arg(self):
        '''Arguments: self
        Return value: None
        Purpose: Tests if usage statement is printed when no arguments are given
        '''
        sys.argv = ['command_line.py']
        self.assertEqual(self.sys_helper(), "Usage: python3 command_line.py [--help]")

    if __name__ == '__main__':
        unittest.main()
