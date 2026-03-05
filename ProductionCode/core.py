'''Handles core features'''
import csv
import io
from ProductionCode.datasource import DataSource

class Features():
    '''
    Purpose: Stores the core features of the website 
    '''
    def __init__(self):
        self.ds = DataSource()

    def average(self, country):
        '''Arguments: country (str)
        Return: The average of the given dataset (str)
        Purpose: To get the average co2 of a subset of data for a country
        '''
        data_set = self.ds.get_average_co2(country)
        return data_set

    def ratio(self, country):
        '''Arguments: country (str)
        Return: A ratio (float) 
        Purpose: Calculates the ratio for co2_per_capita to energy_per_capita
        '''
        avg_co2 = float(self.ds.get_average_co2_per_capita(country).split()[1])
        avg_energy = float(self.ds.get_average_energy_per_capita(country).split()[1])
        ratio = avg_co2/avg_energy
        return ratio

    def year_co2(self, year_args):
        '''Arguments: self, year_arg, a year (string)
        Return: A list of lists (string) with each country and
        total CO2 emissions from a specific year
        Purpose: To get the total CO2 emissions of each country
        in the dataset from a specific year
        '''
        output = []
        data = self.ds.get_year_co2(year_args)
        final_data = self.csv_helper(data)
        #If information about co2 is not empty
        for row in final_data:
            output.append(row)
        return output

    def year_energy(self, year_args):
        '''Arguments: year_arg, a year (string)
        Return: A list of lists (string) with each country and
        total energy emissions from a specific year
        Purpose: To get the total energy emissions of each country
        in the dataset from a specific year
        '''
        output = []
        data = self.ds.get_year_energy(year_args)
        final_data = self.csv_helper(data)

        for row in final_data:
            output.append(row)
        return output

    def highest_biofuel(self, biofuel_arg):
        '''Argument: biofuel_arg (str), a country name
        Return: int highest emissions
        Purpose: Returns a single int representing the highest
        biofuel electricity usage of a specific country
        '''
        max_biofuel = self.ds.get_biofuel(biofuel_arg)
        return max_biofuel

    def country_co2 (self, country):
        '''Argument: country (str)
        Return: A list of data from co2_data for a specific country
        Purpose: To get all of the data in 
        the database for a specific country
        '''
        output = []
        data = self.ds.get_country_co2(country)
        final_data = self.csv_helper(data)

        for row in final_data:
            output.append(row)
        return output

    def csv_helper(self, data):
        '''Argument: data (exported csv from SQL query)
        Return: csv reader
        Purpose: To reduce duplicate code
        '''
        csv_file = io.StringIO(data)
        reader = csv.reader(csv_file)
        next(reader) #skips col name
        return reader
