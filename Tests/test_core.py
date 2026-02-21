'''modules for testing basic_cl.py main function'''
import unittest
from unittest.mock import patch, MagicMock
from ProductionCode.core import Features

class TestCore(unittest.TestCase):
    '''Arguments: unittest.TestCase
    Return value: none
    Purpose: Holds the tests for core.py
    Run with: python -m unittest Tests/test_core.py
    '''
    core = Features()

    def test_average(self):
        '''Arguments: self (TestCore)
        Return: none
        Purpose: Tests the core feature average
        '''
        #Average for Canada cumulative_co2
        self.assertAlmostEqual(self.core.average("Canada"), "148.5173125")

    def test_ratio(self):
        '''Arguments: self (TestCore)
        Return: none
        Purpose: Tests the core ratio function
        '''
        self.assertAlmostEqual(self.core.ratio("Japan"), 9.602605207949379e-05)

    @patch('ProductionCode.datasource.records.Database')
    def test_year_co2(self):
        '''Arguments: self (TestCore)
        Return: none
        Purpose: Tests the year_co2 core feature
        '''
        mock_db_instance = mock_db_class.return_value
        records_object = MagicMock()
        records_object.export.return_value = "Canada,2000,1.1"
        mock_db_instance.query.return_value = records_object

        results = core.year_co2("2000")
        self.assertEqual(results, [['Canada','2000', '1.1']])

        mock_db_instance.query.return_value = records_object

    # def test_year_co2_edge(self):
    #     '''Arguments: self (TestCommandLine)
    #     Return: none
    #     Purpose: Tests edge cases for the year_co2 function in command_line.py
    #     '''
    #     self.assertEqual(self.core.year_co2(2004, [],3), [])
    #     self.assertEqual(self.core.year_co2("Canadaa", [],3), [])

    def test_highest_biofuel(self):
        '''Arguments: self (TestCore)
        Return: none
        Purpose: Tests highest_biofuel function from core
        '''
        self.assertEqual(self.core.highest_biofuel("Canada"), 33.705)

    def test_biofuel_edge(self):
        '''Arguments: self (TestCore)
        Return: none
        Purpose: Tests edge case for highest_biofuel feature in core
        '''
        self.assertEqual(self.core.highest_biofuel("Uruguay"), "No data found")
