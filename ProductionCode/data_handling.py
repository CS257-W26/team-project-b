import csv

class Data_Handler:

    def __init__(self):
        self.data = []

    def load_data(self, dataset):
        '''
        Purpose: Load data for other functions in this file
        '''
        self.data.clear()
        with open(dataset, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                self.data.append(row)
        return self.data
    
    def extract_row(self, country):
        '''Argument: self, country (str)
        Purpose: Extracts a row from the dataset based on country
        Returns: A list
        '''
        country_data = []
        for row in self.data:
            if (row[0] == country):
                country_data.append(row)
        return country_data
        
    def clean_column(self, col, dataset):
        '''Argument: self, column to clean (col)
        Purpose: Returns a clean column with only necessary data
        Return: A list 
        '''
        cleaned_col = []
        for row in dataset:
            if row[col] != '':
                cleaned_col.append(row[col])
        return cleaned_col

    def convert_type(self, value_list):
        '''
        Purpose: Convert column from str to float type
        Return: A list of float values
        '''
        index = -1
        for i in value_list:
            index += 1
            value_list[index] = float(i)
        return value_list

    def set_data(self, dataset, country, col):
        '''Argument: country (Str)
        '''
        self.load_data(dataset)

        cleaned = self.clean_column(col, self.extract_row(country))
        
        final_data = self.convert_type(cleaned)

        return final_data