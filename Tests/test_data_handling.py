import unittest
from ProductionCode.data_handling import DataHandler

class TestDataHandling(unittest.TestCase):
    '''Argument: unittest.TestCase
    Return value: None
    Purpose: Holds the test for the data handling file
    '''
    data = DataHandler()

    data.load_data('Data/dummy_energy_data.csv')

    def test_load_data(self):
        '''Argument: self
        Return: None
        Purpose: Tests if load_data function properly loads csv data
        '''
        self.assertEqual(self.data.load_data('Data/dummy_data.csv'), 
        [["Canada", "2004", "1.452", "12.345"],
        ["Canada", "1998", "2.045", "10.432"],
        ["Canada", "2018", "3.192", "15.725"],
        ["Japan", "2004", "1.133", "12.333"],
        ["Japan", "1998", "0.792", "8.324"],
        ["Japan", "2018", "9.034", "20.324"],
        ["Argentina", "2004", "0.630", "1.234"],
        ["Argentina", "1998", "1.582", "9.87"],
        ["Argentina", "2018","",""],
        ["Argentina","2019","1.609", "10.23"]])

    def test_extract_row(self):
        '''Argument: self
        Return: None
        Purpose: Tests if function extracts correct country row
        '''
        self.assertEqual(self.data.extract_row("Japan"), 
        [['Japan', '2004', '1.133', '4.359'],
        ['Japan', '1998', '0.792' , '24.132'],
        ['Japan', '2018', '9.034' , '45.32']])
    
    def test_clean_column(self):
        '''Argument: self
        Return: None
        Purpose: Tests if clean_column returns appropriate 
        column with no white space
        '''
        self.assertEqual(self.data.clean_column(2, 
        [['Japan', '2004', '', '4.359'], 
        ['Japan', '1998', '', '24.132'],
        ['Japan', '2018', '9.034', '45.32']]),
        ["9.034"])
    
    def test_convert_type(self):
        '''Argument: self
        Return: None
        Purpose: Tests if conversion of str to float works appropriately
        '''
        self.assertEqual(self.data.convert_type(["9.034", "19.213", "11"]), 
        [9.034, 19.213, 11])