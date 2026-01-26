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
    pass


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
