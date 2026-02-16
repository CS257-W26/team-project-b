'''modules for testing basic_cl.py main function'''
import unittest
from unittest.mock import patch, MagicMock
from ProductionCode.datasource import DataSource

class TestDatasource (unittest.TestCase):
    '''Argument: unittest.TestCase
    Return: None
    Purpose: Holds tests for datasource.py
    '''
    data_source = DataSource()

    @patch ('ProductionCode.datasource.records.Database')
    def test_get_country_co2(self, mock_db_class):
        '''Argument: self, mock_db_class
        Return: None
        Purpose: Sets and tests mock data for get_country_co2
        '''
        mock_db_instance = mock_db_class.return_value
        mock_row1 = MagicMock()
        #mock_row2 = MagicMock()
        #mock_row3 = MagicMock()
        mock_row1.export.return_value = "Canada,1,1,1"
        #mock_row2.export.return_value = "Canada,1,2,3"
        #mock_row3.export.return_value = "Japan,1,1,1"
        mock_db_instance.query.return_value = [mock_row1]
        ds = DataSource()
        result = ds.get_country_co2('Canada')
        mock_db_instance.query.assert_called_once_with(
        "SELECT * FROM co2_data WHERE country = 'Canada'")
        mock_row1.export.assert_called_with('csv')
        #mock_row2.export.assert_called_with('csv')
        #mock_row3.export.assert_called_with('csv')
        self.assertEqual(result, "Canada,1,1,1")

    @patch ('ProductionCode.datasource.records.Database')
    def test_get_country_energy(self, mock_db_class):
        '''Argument: self, mock_db_class
        Return: None
        Purpose: Sets and tests mock data for get_country_energy
        '''
        mock_db_instance = mock_db_class.return_value
        mock_row1 = MagicMock()
        mock_row1.export.return_value = "Canada,1,1,1"
        mock_db_instance.query.return_value = [mock_row1]
        ds = DataSource()
        result = ds.get_country_energy('Canada')
        mock_db_instance.query.assert_called_once_with(
        "SELECT * FROM energy_data WHERE country = 'Canada'")
        mock_row1.export.assert_called_with('csv')
        self.assertEqual(result, "Canada,1,1,1")
