class Features():
    '''
    Purpose: Stores the core features of the website 
    '''

    def average(self, dataset):
        '''Arguments: dataset (list of values)
        Return: The average of the given dataset (str)
        Purpose: To get the average of a subset of data for a country
        '''
        total = 0
        count = 0
        for row in dataset:
            if isinstance(row,float):
                total += row
                count += 1
        if count == 0:
            return 'No data found'
        return str((total/count))

    def ratio(self, dataset1, dataset2):
        '''Arguments: country (year)
        Return: A ratio (float) 
        Purpose: Calculates the ratio for co2_per_capita to energy_per_capita
        '''
        avg_co2 = float(self.average(dataset1))
        avg_energy = float(self.average(dataset2))
        ratio_variable = avg_co2/avg_energy
        return ratio_variable

    def year_co2 (self,year, dataset):
        '''Arguments: year (string)
        Return: A list of lists (string) with each country and
        total CO2 emissions from a specific year
        Purpose: To get the total CO2 emissions of each country
        in the dataset from a specific year
        '''
        output = []

        if isinstance(year, str):
            for row in dataset:
                country = row[0]
                year_row = row[1]
                co2 = row[2]
                if year_row == (year) and co2 != "":
                    output.append([country, year_row, co2])
        return output

    def highest_biofuel(self, values):
        '''Argument: values (list)
        Return: int highest emissions
        Purpose: Returns a single int representing the highest
        biofuel consumption of a specific country
        '''
        biofuel = -1
        if isinstance(values, list):
            for num in values:
                if isinstance(num,float) and num > biofuel:
                    biofuel = num
            return biofuel
        if biofuel == -1:
            return 'Invalid input'
        return biofuel
