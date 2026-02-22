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

    def sys_helper(self):
        '''Arguments: self
        Return value: Returns sys.stdout output (str)
        Purpose: Reduces duplicated code by returning output from sys.stdout
        '''
        sys.stdout = StringIO()
        main()
        return sys.stdout.getvalue().strip()

    def test_main(self):
        '''Arguments: self (TestProductionCode)
        Return value: None
        Purpose: Tests whether the main function returns the correct value for the
        specified function in command line arguments
        '''
        #Testing for arg_ratio
        sys.argv = ['command_line.py','--ratio','Japan']
        self.assertEqual(self.sys_helper(), "9.602605207949379e-05")

        #Testing for arg_average
        sys.argv = ['command_line.py', '--average', 'Canada']
        self.assertEqual(self.sys_helper(), '148.5173125')

        #Testing for arg_biofuel
        sys.argv = ['command_line.py', '--biofuel', 'Canada']
        self.assertEqual(self.sys_helper(), '33.705')

        #Testing for arg year_co2
        # sys.argv = ['command_line.py', '--year_co2', '1998']
        # self.assertEqual(self.sys_helper(),
        # 'Annual CO2 emissions (measured in million tonnes) in the year 2019: Argentina: 1.609')

        #Testing for no arg
        sys.argv = ['command_line.py']
        self.assertEqual(self.sys_helper(), "Usage: python3 command_line.py [--help]")

    def test_arg_year_co2(self):
        '''Arguments: self (TestProductionCode)
        Return value: None
        Purpose: Tests if year_co2 argument in main displays correct output
        '''
        sys.argv = ['command_line.py', '--year_co2', '1998']
        self.assertEqual(self.sys_helper(),
        'Annual CO2 emissions (measured in million tonnes) in the year 2019: Argentina: 1.609')



    if __name__ == '__main__':
        unittest.main()
