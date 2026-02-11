'''Purpose: csv module used to read csv file'''
import csv

class DataHandler:
    '''Purpose: Handles the processing of data
    '''

    def __init__(self):
        self.co2_data = self.load_data('owid-co2-data')
        self.energy_data = self.load_data('owid-energy-data')

    def load_data(self, dataset):
        '''Argument: dataset (str)
        Purpose: Load data for other functions in this file
        Return: A list
        '''
        data = []
        with open(dataset, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                self.data.append(row)
        return data data

    def extract_row(self, extraction, column_basis):
        '''Argument: self, extraction (str), column_basis (int)
        Purpose: Extracts a row from the dataset based on extraction (country/year) 
        Returns: A list
        '''
        extraction_data = []
        if isinstance(column_basis, int) and column_basis < len(self.data):
            for row in self.data:
                if row[column_basis] == extraction:
                    extraction_data.append(row)
        return extraction_data

    def clean_column(self, col, dataset):
        '''Argument: self, col (int), dataset (list)
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
        Arguments: self, value_list (list)
        Purpose: Convert list from str to float type
        Return: A list of float values
        '''
        index = -1
        for i in value_list:
            index += 1
            value_list[index] = float(i)
        return value_list

    def set_data(self, dataset, country, col):
        '''Argument: dataset (list), country (Str), col (int)
        Purpose: Has a list of data for a specific country for a specific column
        Return: final_data (list)
        '''
        cleaned = self.clean_column(col, self.extract_row(country))

        final_data = self.convert_type(cleaned)

        return final_data
