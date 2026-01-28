class Averager(self):

    def average(country,dataset,col):
        '''Arguments: country (string)
        Return: The average CO2 emissions of a country (float), 
        or a correction of how this function should work (string)
        Purpose: To get the average CO2 emissions of a country
        '''
        load_data(dataset)
        total = 0
        count = 0
        if isinstance(country, str):
            for row in data:
                if (row[0] == country) and (row[col] != ''):
                    total += float(row[col])
                    count += 1
        else:
            return 'Please input a string for a country'
        if count == 0:
            return 'Please input a valid country'
        return float (total/count)

