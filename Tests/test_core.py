'''modules for testing basic_cl.py main function'''
import unittest
from unittest.mock import patch
from ProductionCode.core import Features

class TestCore(unittest.TestCase):
    '''Arguments: unittest.TestCase
    Purpose: Holds the tests for core.py
    Run with: python -m unittest Tests/test_core.py
    '''

    @patch('ProductionCode.core.DataSource')
    def test_average(self, mock_db_class):
        '''Arguments: self (TestCore), mock_db_class
        Return: none
        Purpose: Tests the core feature average
        '''
        mock_db_instance = mock_db_class.return_value

        mock_db_instance.get_average_co2.return_value = "avg,\r2.0"
        core = Features()
        results = core.average("Canada")

        self.assertEqual(results, "2.0")

    @patch('ProductionCode.core.DataSource')
    def test_ratio(self, mock_db_class):
        '''Arguments: self (TestCore), mock_db_class
        Return: none
        Purpose: Tests the core ratio function
        '''
        mock_db_instance = mock_db_class.return_value
        mock_db_instance.get_average_co2_per_capita.return_value = "Japan, 11"
        mock_db_instance_two = mock_db_class.return_value
        mock_db_instance_two.get_average_energy_per_capita.return_value = "Japan, 20"
        core = Features()
        results = core.ratio("Japan")
        self.assertEqual(results, 0.55)

    @patch('ProductionCode.core.DataSource')
    def test_year_co2(self, mock_db_class):
        '''Arguments: self (TestCore), mock_db_class
        Return: none
        Purpose: Tests the year_co2 core feature
        '''
        mock_db_instance = mock_db_class.return_value

        mock_db_instance.get_year_co2.return_value = "country,year,co2\nCanada,2000,2.1"
        core = Features()
        results = core.year_co2("2000")

        expected = [['Canada', '2000', '2.1']]

        self.assertEqual(results, expected)

    @patch('ProductionCode.core.DataSource')
    def test_year_energy(self, mock_db_class):
        '''Arguments: self (TestCore), mock_db_class
        Return: none
        Purpose: Tests the year_energy core feature
        '''
        mock_db_instance = mock_db_class.return_value

        mock_db_instance.get_year_energy.return_value = "country,year,gas\nCanada,2000,4.7"
        core = Features()
        results = core.year_energy("2000")

        expected = [['Canada', '2000', '4.7']]

        self.assertEqual(results, expected)

    @patch('ProductionCode.core.DataSource')
    def test_highest_biofuel(self, mock_db_class):
        '''Arguments: self (TestCore), mock_db_class
        Return: none
        Purpose: Tests highest_biofuel function from core
        '''
        mock_db_instance = mock_db_class.return_value

        mock_db_instance.get_biofuel.return_value = 33.705
        core = Features()
        results = core.highest_biofuel("Canada")
        self.assertEqual(results, 33.705)

    @patch('ProductionCode.core.DataSource')
    def test_biofuel_edge(self, mock_db_class):
        '''Arguments: self (TestCore), mock_db_class
        Return: none
        Purpose: Tests edge case for highest_biofuel feature in core
        '''
        mock_db_instance = mock_db_class.return_value

        mock_db_instance.get_biofuel.return_value = " "
        core = Features()
        results = core.highest_biofuel("Uruguay")
        self.assertEqual(results, " ")

    @patch('ProductionCode.core.DataSource')
    def test_country_co2(self, mock_db_class):
        '''Arguments: self, mock_db_class
        Return: None
        Purpose: Tests to see all related data for a specific country 
        '''
        mock_db_instance = mock_db_class.return_value
        mock_db_instance.get_country_co2.return_value = "country,co2,capita\nCanada,1,2"
        core = Features()
        results = core.country_co2("Canada")
        self.assertEqual(results, [['Canada','1','2']])
