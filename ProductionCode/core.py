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

    def average(self,country,dataset,col):
        '''Arguments: country (string)
        Return: The average CO2 emissions of a country (float), 
        or a correction of how this function should work (string)
        Purpose: To get the average CO2 emissions of a country
        '''
        self.load_data(dataset)
        total = 0
        count = 0
        if isinstance(country, str):
            for row in self.data:
                if (row[0] == country) and (row[col] != ''):
                    total += float(row[col])
                    count += 1
        else:
            return 'Please input a string for a country'
        if count == 0:
            return 'Please input a valid country'
        return float (total/count)

    def ratio(self,country):
        '''Arguments: country (year)
        Return: A ratio (float) 
        Purpose: Calculates the ratio for co2 and co2 per capita
        '''
        avg_co2 = self.average(country,'Data/dummy_data.csv',3)
        avg_energy = self.average(country,'Data/dummy_energy_data.csv',3)
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
        else:
            return "Please input a valid year"
        if len(year) != 4:
            return "Please input a valid year"
        return output

    def highest_biofuel_consumption(self,country):
        '''Argument: country (String)
        Return: int highest emissions
        Purpose: Returns a single int representing the highest
        biofuel consumption of a specific country
        '''
        biofuel = 0
        if isinstance(country, str):
            for row in self.load_data("Data/dummy_energy_data.csv"):
                if (row[0] == country and row[2] != ''):
                    biofuel = max(biofuel, float(row[2]))
            return biofuel

        return "Invalid input"

