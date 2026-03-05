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
    def test_get_country(self, mock_db_class):
        '''Argument: self, mock_db_class
        Return: None
        Purpose: Sets and tests mock data for get_country
        '''
        mock_db_instance = mock_db_class.return_value
        mock_list = MagicMock()
        mock_list.export.return_value = "Canada,1,1,1\nCanada,2,2,2"
        mock_db_instance.query.return_value = mock_list
        ds = DataSource()
        result = ds.get_country_co2('Canada')
        mock_db_instance.query.assert_called_once_with(
        "SELECT * FROM co2_data WHERE country = 'Canada'")
        mock_list.export.assert_called_with('csv')

        self.assertEqual(result, "Canada,1,1,1\nCanada,2,2,2")

    @patch ('ProductionCode.datasource.records.Database')
    def test_get_country_energy(self, mock_db_class):
        '''Argument: self, mock_db_class
        Return: None
        Purpose: Sets and tests mock data for get_country_energy
        '''
        mock_db_instance = mock_db_class.return_value
        mock_list = MagicMock()
        mock_list.export.return_value = "Canada,1,1,1\nCanada,1,2,3"
        mock_db_instance.query.return_value = mock_list
        ds = DataSource()
        result = ds.get_country_energy('Canada')
        mock_db_instance.query.assert_called_once_with(
        "SELECT * FROM energy_data WHERE country = 'Canada'")
        mock_list.export.assert_called_with('csv')
        self.assertEqual(result, "Canada,1,1,1\nCanada,1,2,3")

    @patch ('ProductionCode.datasource.records.Database')
    def test_get_year_co2(self, mock_db_class):
        '''Argument: self, mock_db_class
        Return: None
        Purpose: Sets and tests mock data for get_country_energy
        '''
        mock_db_instance = mock_db_class.return_value
        mock_list = MagicMock()
        mock_list.export.return_value = "Canada,2000,1,1\nCanada,2000,2,3"
        mock_db_instance.query.return_value = mock_list
        ds = DataSource()
        result = ds.get_year_co2('2000')
        mock_db_instance.query.assert_called_once_with(
            "SELECT country, year, co2, co2_per_capita FROM co2_data WHERE year = '2000'"
        )
        mock_list.export.assert_called_with('csv')
        self.assertEqual(result, "Canada,2000,1,1\nCanada,2000,2,3")

    @patch('ProductionCode.datasource.records.Database')
    def test_get_year_energy(self, mock_db_class):
        '''Argument: self, mock_db_class
        Return: None
        Purpose: Sets and tests mock data for get_year_energy
        '''
        mock_db_instance = mock_db_class.return_value
        mock_list = MagicMock()
        mock_list.export.return_value = "Canada,2000,1,1\nCanada,2000,2,3"
        mock_db_instance.query.return_value = mock_list
        ds = DataSource()
        result = ds.get_year_energy('2000')
        mock_db_instance.query.assert_called_once_with(
            """SELECT country, year, gas_electricity, 
            energy_per_capita FROM energy_data WHERE year = '2000'"""
        )
        mock_list.export.assert_called_with('csv')
        self.assertEqual(result, "Canada,2000,1,1\nCanada,2000,2,3")

    @patch('ProductionCode.datasource.records.Database')
    def test_get_biofuel(self, mock_db_class):
        '''Argument: self, mock_db_class
        Return: None
        Purpose: Sets and tests mock data for get_biofuel
        '''
        mock_db_instance = mock_db_class.return_value
        mock_list = MagicMock()
        mock_list.export.return_value = "5.6"
        mock_db_instance.query.return_value = mock_list
        ds = DataSource()
        result = ds.get_biofuel('Canada')
        mock_db_instance.query.assert_called_once_with(
            "SELECT MAX(biofuel_electricity) FROM energy_data WHERE country = 'Canada'"
        )
        mock_list.export.assert_called_with('csv')
        self.assertEqual(result, "5.6")

    @patch('ProductionCode.datasource.records.Database')
    def test_get_average_co2_per_capita(self, mock_db_class):
        '''Argument: self, mock_db_class
        Return: None
        Purpose: Sets and tests mock data for get_average_co2_per_capita
        '''
        mock_db_instance = mock_db_class.return_value
        mock_list = MagicMock()
        mock_list.export.return_value = "1.333"
        mock_db_instance.query.return_value = [mock_list]
        ds = DataSource()
        result = ds.get_average_co2_per_capita('Canada')
        mock_db_instance.query.assert_called_once_with(
            "SELECT AVG(co2_per_capita) FROM co2_data WHERE country = 'Canada'"
        )
        self.assertEqual(result, "1.333")

    @patch('ProductionCode.datasource.records.Database')
    def test_get_average_energy_per_capita(self, mock_db_class):
        '''Argument: self, mock_db_class
        Return: None
        Purpose: Sets and tests mock data for get_average_energy_per_capita
        '''
        mock_db_instance = mock_db_class.return_value
        mock_list = MagicMock()
        mock_list.export.return_value = "2.222"
        mock_db_instance.query.return_value = [mock_list]
        ds = DataSource()
        result = ds.get_average_energy_per_capita('Canada')
        mock_db_instance.query.assert_called_once_with(
            "SELECT AVG(energy_per_capita) FROM energy_data WHERE country = 'Canada'"
        )
        self.assertEqual(result, "2.222")

    @patch('ProductionCode.datasource.records.Database')
    def test_get_average_co2(self, mock_db_class):
        '''Argument: self, mock_db_class
        Return: None
        Purpose: Sets and tests mock data for get_average_co2
        '''
        mock_db_instance = mock_db_class.return_value
        mock_list = MagicMock()
        mock_list.export.return_value = "3.33"
        mock_db_instance.query.return_value = [mock_list]
        ds = DataSource()
        result = ds.get_average_co2('Canada')
        mock_db_instance.query.assert_called_once_with(
            "SELECT AVG(co2) FROM co2_data WHERE country = 'Canada'"
        )
        self.assertEqual(result, "3.33")
