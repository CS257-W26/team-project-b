import csv

class Features():

    data=[]

    def load_data(self,dataset):
        '''
        Purpose: Load data for other functions in this file
        '''
        self.data.clear()
        with open(dataset, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                self.data.append(row)
        return self.data

    def average(self, dataset):
        '''Arguments: dataset (list of values)
        Return: The average CO2 emissions of a country (float), 
        or a correction of how this function should work (string)
        Purpose: To get the average CO2 emissions of a country
        '''
        total = 0
        count = 0
        for row in dataset:
            total += row
            count += 1
        return str((total/count))


    def ratio(self, country, dataset):
        '''Arguments: country (year)
        Return: A ratio (float) 
        Purpose: Calculates the ratio for co2 and co2 per capita
        '''
<<<<<<< HEAD
        avg_co2 = self.average(country,'Data/dummy_data.csv',3)
        avg_energy = self.average(country,'Data/dummy_energy_data.csv',3)
=======
        avg_co2 = self.average('Data/dummy_data.csv')
        avg_energy = self.average('Data/dummy_energy_data.csv')
>>>>>>> be055634a2c35ff3d1b29c7d422d213afe5c5e5a
        ratio_variable = avg_co2/avg_energy
        return ratio_variable

    def year_co2 (self,year):
        '''Arguments: year (string)
        Return: A list of lists (string) with each country and
        total CO2 emissions from a specific year
        Purpose: To get the total CO2 emissions of each country
        in the dataset from a specific year
        '''
        self.load_data("Data/dummy_data.csv")

        output = []

        if isinstance(year, str):
            for row in self.data:
                country = row[0]
                year_row = row[1]
                co2 = row[2]
                if year_row == (year) and co2 != "":
                    output.append([country, year_row, co2])
        return output

    def highest_biofuel(self, values):
        '''Argument: country (String)
        Return: int highest emissions
        Purpose: Returns a single int representing the highest
        biofuel consumption of a specific country
        '''
        biofuel = 0
        for num in values:
            if num > biofuel:
                biofuel = num
        return biofuel

