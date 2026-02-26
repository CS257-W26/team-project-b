from flask import Flask, Blueprint
from ProductionCode.core import Features

core = Features()
app = Flask(__name__)
api = Blueprint('api', __name__) #api object

@app.route("/")
def homepage():
    '''
    Purpose: homepage to show instructions for available routes
    '''
    return "Welcome to Emission Tracker!\
    To view CO2 data from 2004 (or 1998/2018),\
    enter the following: /year_co2/2004 \n\
    To view the highest biofuel consumption for a country,\
    enter the following: /biofuel/Canada"

@app.errorhandler(404)
def page_not_found(e):
    '''
    Purpose: Handles user error if wrong format is inputted
    '''
    message = " Try: /api/year_co2/2004, /api/biofuel/Canada"
    return str(e) + message

@api.route("/average/<country>")
def route_api_average(country):
    '''Arguments: country (string)
    Return: The average CO2 emissions of a country (float), 
    or a correction of how this function should work (string)
    Purpose: Display the average CO2 emissions of a country
    '''
    average = core.average(country)
    print ("Printed")
    # output = "The average annual CO2 emissions (measured in million tonnes) for " + country + ": "
    return str(average)

@api.route("/ratio/<country>")
def route_api_ratio(country):
    '''Arguments: country (year)
    Return: A ratio (float) 
    Purpose: Display the ratio for co2_per_capita to energy_per_capita
    '''
    ratio = core.ratio(country)

    # output = (
    #     "The ratio between averages of annual CO2 per capita (tonnes per person)"
    #     " to energy use per capita (kilowatt-hours per person) for " + country + ": "
    # )

    return str(ratio)

@api.route("/year_co2/<year>")
def route_api_year_co2(year):
    '''Arguments: year (string)
    Return: A list of lists (string) with each country and
    total CO2 emissions from a specific year
    Purpose: To display the total CO2 emissions of each country
    in the dataset from a specific year
    '''
    result = core.year_co2(year)

    return result

@api.route("/year_energy/<year>")
def route_api_year_energy(year):
    '''Arguments: year (string)
    Return: A list of lists (string) with each country and
    total CO2 emissions from a specific year
    Purpose: To display the total CO2 emissions of each country
    in the dataset from a specific year
    '''
    result = core.year_energy(year)

    return result

@api.route("/biofuel/<country>")
def route_api_biofuel(country):
    """
    Arguments: country (string)
    Return: inputted country by user (string) and highest biofuel 
    consumption value of that country (string)
    Purpose: Display the highest biofuel consumption for the given country
    """
    result = core.highest_biofuel(country)

    # output = "Highest biofuel consumption (measured in terawatt-hours) for " + country + " is: "
    return str(result)
