'''
The eventual location for the Flask app interface for the project.
'''
from flask import Flask, render_template, request
from ProductionCode.core import Features
from flask_api import ApiFunctions

app = Flask(__name__)
core = Features()
api = ApiFunctions()

@app.route("/")
def homepage():
    '''
    Purpose: homepage to show instructions for available routes
    '''
    return render_template('header.html', title = "Emission Tracker")

@app.errorhandler(404)
def page_not_found(e):
    '''
    Purpose: Handles user error if wrong format is inputted
    '''
    message = " Try: /api/year_co2/2004, /api/biofuel/Canada"
    return str(e) + message

@app.route("/average/<country>")
def route_average(country):
    '''Arguments: country (string)
    Return: The average CO2 emissions of a country (float), 
    or a correction of how this function should work (string)
    Purpose: Display the average CO2 emissions of a country
    '''
    average = api.route_average(country)
    return render_template('functions.html', function = "average",
    input = country, output = average)

@app.route("/ratio/<country>")
def route_ratio(country):
    '''Arguments: country (year)
    Return: A ratio (float) 
    Purpose: Display the ratio for co2_per_capita to energy_per_capita
    '''
    ratio = api.route_ratio(country)
    return render_template('ratio_function.html', country_html = country, output = ratio)

@app.route("/year_co2/<year>")
def route_year_co2(year):
    '''Arguments: year (string)
    Return: A list of lists (string) with each country and
    total CO2 emissions from a specific year
    Purpose: To display the total CO2 emissions of each country
    in the dataset from a specific year
    '''
    result = api.route_year_co2(year)
    return render_template('year_function.html', title = 'Year CO2', year_html = year, output = result)

@app.route("/year_energy/<year>")
def route_year_energy(year):
    '''Arguments: year (string)
    Return: A list of lists (string) with each country and
    total CO2 emissions from a specific year
    Purpose: To display the total CO2 emissions of each country
    in the dataset from a specific year
    '''
    result = api.route_year_energy(year)
    return render_template('year_function.html', title = 'Year Energy', year_html = year, output = result)

@app.route("/biofuel/<country>")
def route_biofuel(country):
    """
    Arguments: country (string)
    Return: inputted country by user (string) and highest biofuel 
    consumption value of that country (string)
    Purpose: Display the highest biofuel consumption for the given country
    """
    result = api.route_biofuel(country)
    return render_template('biofuel_function.html', country_html = country, output = result)

if __name__ == "__main__":
    app.register_blueprint(api, url_prefix='/api')
    app.run(host='0.0.0.0', port=5113)
