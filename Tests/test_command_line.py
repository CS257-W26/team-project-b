'''modules for testing basic_cl.py main function'''
import sys
import unittest
from io import StringIO
from command_line import main

class TestCommandLine(unittest.TestCase):
    '''Arguments: unittest.TestCase
    Return value: none
    Purpose: Holds the tests for command_line.py
    '''
    def test_main(self):
        '''Arguments: self (TestProductionCode)
        Return value: None
        Purpose: Tests whether the main function returns the correct value for the
        specified function in command line arguments
        '''
        sys.argv = ['command_line.py','--ratio','Canada']
        sys.stdout = StringIO()
        main()
        output = sys.stdout.getvalue().strip()

        self.assertEqual(output, "0.46071556778748357")

    def test_main_no_arg(self):
        '''Arguments: self
        Return value: None
        Purpose: Tests if usage statement is printed when no arguments are given
        '''
        sys.argv = ['command_line.py']
        sys.stdout = StringIO()
        main()
        output = sys.stdout.getvalue().strip()

        self.assertEqual(output, "Usage: python3 command_line.py [options]")

    if __name__ == '__main__':
        unittest.main()
