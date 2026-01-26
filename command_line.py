'''
Purpose: Allows user to interact with data with the command line

'''
import csv
import sys
import argparse

data = []

def load_data(dataset):
    '''
    Purpose: Load data for other functions in this file
    '''
    with open(dataset, newline='') as file:
        reader = csv.reader (file)
        for row in reader:
            data.append(row)
    return data

def average_co2 (country):
    '''Arguments: country (string)
    Return: The average CO2 emissions of a country (float), 
    or a correction of how this function should work (string)
    Purpose: To get the average CO2 emissions of a country
    '''
    load_data
    sum = 0
    count = 0
    if type(country) is str:
        for row in data:
            if row[0].equals(country):
                sum += row[2]
                count += 1
    else:
        return 'Please input a string for a country'
    if count == 0:
        return 'Please input a valid country'
    return sum/count


def year_co2 (year):
    '''
    
    '''
    pass

def highest_co2 (country):
    '''
    Purpose: Return the highest co2 emissions for a country 
    
    '''
    pass


def main ():
    '''
    Purpose: 
    '''
    pass
