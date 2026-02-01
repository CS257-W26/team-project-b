'''
The eventual location for the Flask app interface for the project.
'''

from flask import Flask
from ProductionCode.core import load_data, average,ratio,year_co2,highest_biofuel_consumption,load_data, main
from ProductionCode.data_handling import load_data, extract

app = Flask(__name__)

@app.route("/")
def homepage():
    """
    Purpose: homepage to show instructions for available routes
    """
    return """Welcome to Emission Tracker!
    To view CO2 data from 2004 (or 1998/2018),
    enter the following: /year_co2/2004 \n
    To view the highest biofuel consumption for a country,
    enter the following: /biofuel/Canada"""

@app.route("/year_co2/<year>")
def route_year_co2(year):
    '''Arguments: year (string)
    Return: A list of lists (string) with each country and
    total CO2 emissions from a specific year
    Purpose: To display the total CO2 emissions of each country
    in the dataset from a specific year
    '''

    data = year_co2(year)

    output = "CO2 emissions in the year " + year + ": "

    if isinstance(data, str):
        return data

    for row in data:
        country = row[0]
        co2 = row[2]
        if co2 != "":
            output = output + country + ": " + co2 + "\n"

    return output

@app.route("/biofuel/<country>")
def route_biofuel(country):
    """
    Arguments: country (string)
    Return: inputted country by user (string) and highest biofuel 
    consumption value of that country (string)
    Purpose: Display the highest biofuel consumption for the given country
    """
    data = highest_biofuel_consumption(country)
    return "Highest biofuel consumption for " + country + " is " + str(data)

if __name__ == "__main__":
    app.run()
