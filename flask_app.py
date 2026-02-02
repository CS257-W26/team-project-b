'''
The eventual location for the Flask app interface for the project.
'''

from flask import Flask
from ProductionCode.core import Features
from ProductionCode.data_handling import Data_Handler

app = Flask(__name__)
# api = Blueprint('api', __name__)
core = Features()
data_handling = Data_Handler()

@app.route("/")
def homepage():
    """
    Purpose: homepage to show instructions for available routes
    """
    return "Welcome to Emission Tracker!\
    To view CO2 data from 2004 (or 1998/2018),\
    enter the following: /year_co2/2004 \n\
    To view the highest biofuel consumption for a country,\
    enter the following: /biofuel/Canada"

@app.errorhandler(404)
def page_not_found(e):
    return "Sorry, wrong format. Please enter one of the following commands: /year_co2/2004, /biofuel/Canada"

@app.route("/average/<country>")
def route_average(country):
    '''Arguments: country (string)
    Return: The average CO2 emissions of a country (float), 
    or a correction of how this function should work (string)
    Purpose: Display the average CO2 emissions of a country
    '''
    average_list = data_handling.set_data("Data/dummy_data.csv", country, 2)
    average = core.average(average_list)

    output = "The average annual CO2 emissions (measured in million tonnes) for " + country + ": "
    return output + str(average)
    
@app.route("/ratio/<country>")
def route_ratio(country):
    '''Arguments: country (year)
    Return: A ratio (float) 
    Purpose: Display the ratio for co2_per_capita to energy_per_capita
    '''
    co2_data = data_handling.set_data("Data/dummy_data.csv", country, 3)
    co2_per_capita = data_handling.set_data("Data/dummy_energy_data.csv", country, 3)

    ratio = core.ratio(co2_data, co2_per_capita)

    output = "The ratio between averages of annual CO2 per capita (tonnes per person) to energy use per capita (kilowatt-hours per person) for " + country + ": "

    return output + str(ratio)

@app.route("/year_co2/<year>")
def route_year_co2(year):
    '''Arguments: year (string)
    Return: A list of lists (string) with each country and
    total CO2 emissions from a specific year
    Purpose: To display the total CO2 emissions of each country
    in the dataset from a specific year
    '''
    data = core.year_co2(year, data_handling.load_data("Data/dummy_data.csv"))

    output = "Annual CO2 emissions (measured in million tonnes) in the year " + year + ": "

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
    values = data_handling.set_data("Data/dummy_energy_data.csv", country, 2)
    data = core.highest_biofuel(values)

    output = "Highest biofuel consumption (measured in terawatt-hours) for " + country + " is "
    return output + str(data)

if __name__ == "__main__":
    app.run(port = 5013)
    # app.register_blueprint(api, url_prefix='/api')

