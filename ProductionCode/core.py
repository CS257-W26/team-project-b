'''Handles core features'''
from ProductionCode.datasource import DataSource

class Features():
    '''
    Purpose: Stores the core features of the website 
    '''
    def __init__(self):
        self.ds = DataSource()

    def average(self, average_arg):
        '''Arguments: average_arg, a country (str)
        Return: The average of the given dataset (str)
        Purpose: To get the average of a subset of data for a country
        '''
        dataset = self.ds.get_country_co2(average_arg)

        total = 0
        count = 0
        for row in dataset:
            if isinstance(row,float) and row != "":
                total += row
                count += 1
        if count == 0:
            return 'No data found'
        return str((total/count))

    def ratio(self, ratio_arg):
        '''Arguments: ratio_arg, a country (year)
        Return: A ratio (float) 
        Purpose: Calculates the ratio for co2_per_capita to energy_per_capita
        '''
        data1 = self.ds.get_co2_per_capita(ratio_arg)
        data2 = self.ds.get_energy_per_capita(ratio_arg)

        avg_co2 = float(self.average(data1))
        avg_energy = float(self.average(data2))

        ratio_variable = avg_co2/avg_energy
        return ratio_variable

    def year_co2 (self, year_args):
        '''Arguments: year_arg, a year (string)
        Return: A list of lists (string) with each country and
        total CO2 emissions from a specific year
        Purpose: To get the total CO2 emissions of each country
        in the dataset from a specific year
        '''
        output = []
        final_data = self.ds.get_year_co2(year_args)

        for row in final_data:
            if row[2] != "":
                output.append([row[0], row[1], row[2]])
        return output

    def highest_biofuel(self, biofuel_arg):
        '''Argument: biofuel_arg (str), a country name
        Return: int highest emissions
        Purpose: Returns a single int representing the highest
        biofuel consumption of a specific country
        '''
        values = self.ds.get_biofuel(biofuel_arg)

        biofuel = -1
        # if isinstance(values, list):
        for num in values:
            if isinstance(num,float) and num > biofuel:
                biofuel = num
        return values
        
        # if biofuel == -1:
        #     return 'Invalid input'
        # return biofuel
