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

    @patch('command_line.core.ratio')
    def test_arg_ratio(self, mock_ratio):
        '''Arguments: self, mock_ratio
        Return value: None
        Purpose: Tests whether the main function returns the correct value for the
        specified function in command line arguments
        '''
        #Acceptance Test Feature 2: Testing for arg_ratio
        mock_ratio.return_value = "1.33"

        sys.argv = ['command_line.py','--ratio','Japan']
        self.assertEqual(self.sys_helper(), "1.33")

    @patch('command_line.core.average')
    def test_main_arg_average(self, mock_average):
        '''Arguments: self, mock_average
        Return value: None
        Purpose: Testing the return of the correct value for the
        arg_average argument
        '''
        #Testing for arg_average
        mock_average.return_value = "148.516"

        sys.argv = ['command_line.py', '--average', 'Canada']
        self.assertEqual(self.sys_helper(), '148.516')

    @patch('command_line.core.highest_biofuel')
    def test_main_arg_biofuel(self, mock_biofuel):
        '''Arguments: self, mock_biofuel
        Return value: None
        Purpose: Tests the highest_biofuel argument for corrrect output
        '''
        #Acceptance Test Feature 1: Testing for arg_biofuel
        mock_biofuel.return_value = "33.705"
        sys.argv = ['command_line.py', '--biofuel', 'Canada']
        self.assertEqual(self.sys_helper(), '33.705')

    @patch('command_line.core.year_co2')
    def test_main_arg_year_co2(self, mock_year_co2):
        '''Arguments: self, mock_year_co2
        Return value: None
        Purpose: Tests if year_co2 argument in main displays correct output
        '''
        #Acceptance Test Feature 3: Testing for arg year_co2
        mock_year_co2.return_value = "Canada,1998,2.2"
        sys.argv = ['command_line.py', '--year_co2', '1998']
        self.assertEqual(self.sys_helper(), "Canada,1998,2.2")

    def test_no_arg(self):
        '''Argument: self
        Return Value: None
        Purpose: Tests if the help usage statement is printed
        '''
        #Testing for no arg
        sys.argv = ['command_line.py']
        self.assertEqual(self.sys_helper(), "Usage: python3 command_line.py [--help]")

    if __name__ == '__main__':
        unittest.main()
