'''
The eventual location for the Flask app interface for the project.
'''

from flask import Flask
from ProductionCode.core import Features

app = Flask(__name__)
# api = Blueprint('api', __name__)
core = Features()

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

@app.errorhandler(404)
def page_not_found(e):
    return """Sorry, wrong format. Please enter one of the following commands: /year_co2/2004, /biofuel/Canada """

@app.route("/average/<country>")
def route_average(country):
    '''Arguments: country (string)
    Return: The average CO2 emissions of a country (float), 
    or a correction of how this function should work (string)
    Purpose: Display the average CO2 emissions of a country
    '''
    core.load_data(dataset)
    average = core.average(country, "Data/dummy_data.csv", 2)

    if isinstance(average, str):
        return average

    return "The average CO2 emissions (measured in million tonnes) for " + country + " is " + str(average)
    
@app.route("/ratio/<country>")
def route_ratio(country):
    '''Arguments: country (year)
    Return: A ratio (float) 
    Purpose: Display the ratio for co2 and co2 per capita
    '''
    avg_co2 = core.average("Data/dummy_data.csv")
    avg_co2_per_capita = core.average(country,'Data/dummy_energy_data.csv',3)

    output = "The ratio between averages of annual CO2 emissions and CO2 per capita (measured in million tonnes) for " + country + ": "

    ratio_variable = avg_co2/avg_co2_per_capita
    return output + ratio_variable

@app.route("/year_co2/<year>")
def route_year_co2(year):
    '''Arguments: year (string)
    Return: A list of lists (string) with each country and
    total CO2 emissions from a specific year
    Purpose: To display the total CO2 emissions of each country
    in the dataset from a specific year
    '''
    core.load_data("Data/dummy_data.csv")
    data = core.year_co2(year)

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
    data = core.highest_biofuel_consumption(country)
    return "Highest biofuel consumption (measured in terawatt-hours) for " + country + " is " + str(data)

if __name__ == "__main__":
    app.run(port = 5006)
    # app.register_blueprint(api, url_prefix='/api')

