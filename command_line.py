'''
Purpose: Allows user to interact with data with the command line

'''
import csv
import sys
import argparse

def average_co2 (country):
    pass


def year_co2 (year):
    '''
    
    '''
    pass

def highest_co2 (country):
    '''
    Purpose: Return the highest co2 emissions for a country 
    Return: int highest emissions
    '''
    emission = 0
    for row in load_data():
        if row[0] == country:
            if float(row[2]) > emission:
                emission = float(row[2])         
    return emission

def load_data():
    '''
    Purpose: Load data for other functions in this file
    '''
    pass

def main ():
    '''
    Purpose: 
    '''
    pass
