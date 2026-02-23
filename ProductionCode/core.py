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

    def calculate_average(self, data):
        '''Arguments: data (csv reader)
        Return: The average (str)
        Purpose: Calculates the average
        '''
        total = 0
        count = 0
        for row in data:
            if row[0] != "":
                total += float(row[0])
                count += 1
        if count == 0:
            return 'No data found'
        return str((total/count))

    def average(self, average_arg):
        '''Arguments: average_arg, a country (str)
        Return: The average of the given dataset (str)
        Purpose: To get the average co2 of a subset of data for a country
        '''
        data_set = self.ds.get_country_co2(average_arg)
        final_data = self.csv_helper(data_set)

        return self.calculate_average(final_data)

    def ratio(self, ratio_arg):
        '''Arguments: ratio_arg, a country (year)
        Return: A ratio (float) 
        Purpose: Calculates the ratio for co2_per_capita to energy_per_capita
        '''
        csv1 = self.ds.get_co2_per_capita(ratio_arg)
        csv2 = self.ds.get_energy_per_capita(ratio_arg)

        data1 = self.csv_helper(csv1)
        data2 = self.csv_helper(csv2)

        avg_co2 = float(self.calculate_average(data1))
        avg_energy = float(self.calculate_average(data2))

        ratio_variable = avg_co2/avg_energy
        return ratio_variable

    def year_co2(self, year_args):
        '''Arguments: year_arg, a year (string)
        Return: A list of lists (string) with each country and
        total CO2 emissions from a specific year
        Purpose: To get the total CO2 emissions of each country
        in the dataset from a specific year
        '''
        output = []
        data = self.ds.get_year_co2(year_args)
        final_data = self.csv_helper(data)

        for row in final_data:
            if row[2] != "":
                output.append(row)
        return output

    def highest_biofuel(self, biofuel_arg):
        '''Argument: biofuel_arg (str), a country name
        Return: int highest emissions
        Purpose: Returns a single int representing the highest
        biofuel consumption of a specific country
        '''
        data = self.ds.get_biofuel(biofuel_arg)
        final_data = self.csv_helper(data)

        biofuel = -1

        for num in final_data:
            if num[0] != "" and (float(num[0]) > biofuel):
                biofuel = float(num[0])
        if biofuel == -1:
            return "No data found"
        return biofuel

    def csv_helper(self, data):
        '''Argument: data (csv file to read in)
        Return: csv reader
        Purpose: To reduce duplicate code
        '''
        csv_file = io.StringIO(data)
        reader = csv.reader(csv_file)
        next(reader) #skips col name
        return reader