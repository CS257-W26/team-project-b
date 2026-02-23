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

    def mock_helper(self,mock_db_class,data,dataset,expected_value,input,input_set):
        mock_db_instance = mock_db_class.return_value
        mock_list = MagicMock()
        mock_list.export.return_value = expected_value
        mock_db_instance.query.return_value = mock_list
        mock_db_instance.query.assert_called_once_with(
        f"SELECT {data} FROM {dataset} WHERE {input_set} = {input}")
        mock_list.export.assert_called_with('csv')

    @patch ('ProductionCode.datasource.records.Database')
    def test_get_country_co2(self, mock_db_class):
        '''Argument: self, mock_db_class
        Return: None
        Purpose: Sets and tests mock data for get_country_co2
        '''
        self.mock_helper(mock_db_class,"co2","co2_data",
                        "Canada,1,1,1\nCanada,2,2,2",'Canada','country')
        result = self.data_source.get_country_co2('Canada')
        self.assertEqual(result, "Canada,1,1,1\nCanada,2,2,2")

    @patch ('ProductionCode.datasource.records.Database')
    def test_get_country_energy(self, mock_db_class):
        '''Argument: self, mock_db_class
        Return: None
        Purpose: Sets and tests mock data for get_country_energy
        '''
        self.mock_helper(mock_db_class,"energy","energy_data","Canada,1,1,1\nCanada,1,2,3",
                         'Canada','country')
        result = self.data_source.get_country_energy('Canada')
        self.assertEqual(result, "Canada,1,1,1\nCanada,1,2,3")        



    @patch ('ProductionCode.datasource.records.Database')
    def test_get_year_co2(self, mock_db_class):
        '''Argument: self, mock_db_class
        Return: None
        Purpose: Sets and tests mock data for get_country_energy
        '''
        self.mock_helper(mock_db_class,"country, year, co2","co2_data",
                        "Canada,2000,1,1\nCanada,2000,2,3",'2000','year')
        result = self.data_source.get_year_co2(2000)
        self.assertEqual(result, "Canada,2000,1,1\nCanada,2000,2,3")

    @patch('ProductionCode.datasource.records.Database')
    def test_get_year_energy(self, mock_db_class):
        '''Argument: self, mock_db_class
        Return: None
        Purpose: Sets and tests mock data for get_year_energy
        '''
        self.mock_helper(mock_db_class,"country, year, energy","energy_data",
                        "Canada,2000,1,1\nCanada,2000,2,3",'2000','year')
        result = self.data_source.get_year_energy(2000)
        self.assertEqual(result, "Canada,2000,1,1\nCanada,2000,2,3")

    @patch('ProductionCode.datasource.records.Database')
    def test_get_biofuel(self, mock_db_class):
        '''Argument: self, mock_db_class
        Return: None
        Purpose: Sets and tests mock data for get_biofuel
        '''
        self.mock_helper(mock_db_class,"biofuel_consumption","energy_data",
                        "Canada,2000,1,1\nCanada,2000,2,3",'Canada','country')
        result = self.data_source.get_biofuel('Canada')
        self.assertEqual(result, "Canada,2000,1,1\nCanada,2000,2,3")

    @patch('ProductionCode.datasource.records.Database')
    def test_co2_per_capita(self, mock_db_class):
        '''Argument: self, mock_db_class
        Return: None
        Purpose: Sets and tests mock data for get_co2_per_capita
        '''

        self.mock_helper(mock_db_class,"co2_per_capita","co2_data",
                         "Canada,2000,1,1\nCanada,2000,2,3",'Canada','country')
        result = self.data_source.get_biofuel('Canada')
        self.assertEqual(result, "Canada,2000,1,1\nCanada,2000,2,3")

    @patch('ProductionCode.datasource.records.Database')
    def test_energy_per_capita(self, mock_db_class):
        '''Argument: self, mock_db_class
        Return: None
        Purpose: Sets and tests mock data for get_energy_per_capita
        '''
        self.mock_helper(mock_db_class,"energy_per_capita","energy_data",
                         "Canada,2000,1,1\nCanada,2000,2,3",'Canada','country')
        result = self.data_source.get_biofuel('Canada')
        self.assertEqual(result, "Canada,2000,1,1\nCanada,2000,2,3")
