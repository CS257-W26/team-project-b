'''
Purpose: Allows user to interact with data with the command line

'''
import csv
import sys
from io import StringIO
import argparse

data = []

def load_data(dataset):
    '''
    Purpose: Load data for other functions in this file
    '''
    data.clear()
    with open(dataset, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def average(country,dataset,col):
    '''Arguments: country (string)
    Return: The average CO2 emissions of a country (float), 
    or a correction of how this function should work (string)
    Purpose: To get the average CO2 emissions of a country
    '''
    load_data(dataset)
    sum = 0
    count = 0
    if type(country) is str:
        for row in data:
            if (row[0] == country) and (row[col] != ''):
                sum += float(row[col])
                count += 1
    else:
        return 'Please input a string for a country'
    if count == 0:
        return 'Please input a valid country'
    return float (sum/count)

def ratio(country):
    avg_co2 = average(country,'Data/dummy_data.csv',3)
    avg_energy = average(country,'Data/dummy_energy_data.csv',3)
    return avg_co2/avg_energy

def year_co2 (year):
    '''Arguments: year (string)
    Return: A list of lists (string) with each country and 
    total CO2 emissions from a specific year
    Purpose: To get the total CO2 emissions of each country 
    in the dataset from a specific year
    '''
    load_data("Data/dummy_energy_data.csv")

    output = []

    if type(year) is str:
        for row in data:
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


def highest_biofuel_consumption(country):
    '''Argument: country (String)
    Return: int highest emissions
    Purpose: Returns a single int representing the highest 
    biofuel consumption of a specific country 
    '''
    
    biofuel = 0
    if type(country) is str:
        for row in load_data("Data/dummy_energy_data.csv"):
            if (row[0] == country and row[2] != ''):
                if float(row[2]) > biofuel:
                    biofuel = float(row[2])         
        return biofuel
    else:
        return "Invalid input"
        

def main():
    ''' Arguments: none
    Return value:
    Purpose: 
    '''
    sys.stdout = StringIO()

    parser = argparse.ArgumentParser(
        prog = 'command_line.py',
        usage = 'Usage: python3 comand_line.py [options]'
    )
    parser.add_argument('--ratio', nargs = 1, help = 'returns ratio of avg co2_per_capita to energy_per_capita for an inputted country', type = ratio)
    parser.add_argument('--year_co2', nargs = 1, help = 'returns lists of lists country, year, and total co2 emissions for an inputted year')
    parser.add_argument('--biofuel', nargs = 1, help = 'returns an int representing highest biofuel consumption for inputted country')
    