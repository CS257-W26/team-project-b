'''
The eventual location for the Flask app interface for the project.
'''

from flask import Flask, Blueprint, render_template, request
from ProductionCode.core import Features

app = Flask(__name__)
api = Blueprint('api', __name__) #api object
core = Features()

@api.route("/")
def homepage():
    '''
    Purpose: homepage to show instructions for available routes
    '''
    # return "Welcome to Emission Tracker!\
    # To view CO2 data from 2004 (or 1998/2018),\
    # enter the following: /year_co2/2004 \n\
    # To view the highest biofuel consumption for a country,\
    # enter the following: /biofuel/Canada"

    return render_template('header.html', title = "Emission Tracker")

@api.errorhandler(404)
def page_not_found(e):
    '''
    Purpose: Handles user error if wrong format is inputted
    '''
    return str(e) + "Enter one of the following commands: /year_co2/2004, /biofuel/Canada"

@api.route("/average/<country>")
def route_average(country):
    '''Arguments: country (string)
    Return: The average CO2 emissions of a country (float), 
    or a correction of how this function should work (string)
    Purpose: Display the average CO2 emissions of a country
    '''
    average = core.average(country)

    output = "The average annual CO2 emissions (measured in million tonnes) for " + country + ": "
    return output + str(average)

@api.route("/ratio/<country>")
def route_ratio(country):
    '''Arguments: country (year)
    Return: A ratio (float) 
    Purpose: Display the ratio for co2_per_capita to energy_per_capita
    '''
    ratio = core.ratio(country)

    output = (
        "The ratio between averages of annual CO2 per capita (tonnes per person)"
        " to energy use per capita (kilowatt-hours per person) for " + country + ": "
    )

    return output + str(ratio)

@api.route("/year_co2/<year>")
def route_year_co2(year):
    '''Arguments: year (string)
    Return: A list of lists (string) with each country and
    total CO2 emissions from a specific year
    Purpose: To display the total CO2 emissions of each country
    in the dataset from a specific year
    '''
    return core.year_co2(year)

@api.route("/biofuel/<country>")
def route_biofuel(country):
    """
    Arguments: country (string)
    Return: inputted country by user (string) and highest biofuel 
    consumption value of that country (string)
    Purpose: Display the highest biofuel consumption for the given country
    """
    data = core.highest_biofuel(country)

    output = "Highest biofuel consumption (measured in terawatt-hours) for " + country + " is: "
    return output + str(data)

if __name__ == "__main__":
    app.register_blueprint(api, url_prefix='/api')
    app.run(port=5113)
