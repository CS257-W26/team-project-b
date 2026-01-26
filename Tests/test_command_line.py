import unittest
from command_line import average_co2,year_co2,highest_co2,load_data,main

class TestCommandLine (unittest.TestCase):
    def test_load_data (self):
        self.assertEqual (load_data('dummy_data.csv'), [['country', 'year', 'cumulative_co2'], ['Canada', 2004, 1.452],
        ['Canada', 1998, 2.045],
        ['Canada', 2018, 3.192],
        ['Japan', 2000, 1.133],
        ['Japan', 1979, 0.792],
        ['Japan', 1995, 9.034],
        ['Argentina', 1994, 0.630],
        ['Argentina', 2008, 1.582],
        ['Argentina', 2013, ],
        ['Argentina', 2017, 1.609]])
    
    def test_average_co2(self):
        self.assertEqual (average_co2('Canada'),2.22966667)
        self.assertEqual (average_co2('Japan'),10.95900)

    def test_average_co2_edge(self):
        self.assertEqual(average_co2(12), 'Please input a string for a country')
        self.assertEqual(average_co2(''), 'Please input a valid country')
