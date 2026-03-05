'''
The eventual location for the Flask app interface for the project.
'''
from flask import Flask, render_template, request
from ProductionCode.core import Features
from flask_api import (route_api_average, route_api_ratio,
route_api_year_co2, route_api_year_energy, route_api_biofuel, api)

app = Flask(__name__)
core = Features()


@app.route("/")
def homepage():
    '''
    Purpose: homepage to show instructions for available routes
    '''
    return render_template('homepage.html', title = "Emission Tracker")

@app.errorhandler(404)
def page_not_found(e):
    '''
    Purpose: Handles user error if wrong format is inputted
    '''
    return render_template('404.html'), str(e)

@app.route("/action_page")
def action_page():
    '''
    Purpose: Handles user input in the homepage
    '''

@app.route("/average")
def route_average():
    '''Arguments: country (string)
    Return: The average CO2 emissions of a country (float), 
    or a correction of how this function should work (string)
    Purpose: Display the average CO2 emissions of a country
    '''
    country = str(request.args['average_country'])
    average = route_api_average(country)
    return render_template('average_function.html', function = "average",
                           country_html = country, output = average)

@app.route("/ratio")
def route_ratio():
    '''Arguments: country (year)
    Return: A ratio (float) 
    Purpose: Display the ratio for co2_per_capita to energy_per_capita
    '''
    country = str(request.args['ratio_country'])
    ratio = route_api_ratio(country)
    return render_template('ratio_function.html', country_html = country, output = ratio)

@app.route("/year_co2")
def route_year_co2():
    '''Arguments: year (string)
    Return: A list of lists (string) with each country and
    total CO2 emissions from a specific year
    Purpose: To display the total CO2 emissions of each country
    in the dataset from a specific year
    '''
    year = str(request.args['co2_year'])
    result = route_api_year_co2(year)
    return render_template('year_function.html', title = 'Yearly CO₂ Data',
                           year_html = year, output = result)

@app.route("/year_energy")
def route_year_energy():
    '''Arguments: year (string)
    Return: A list of lists (string) with each country and
    total energy emissions from a specific year
    Purpose: To display the total energy emissions of each country
    in the dataset from a specific year
    '''
    year = str(request.args['energy_year'])
    result = route_api_year_energy(year)
    return render_template('year_energy_function.html', title = 'Year Energy',
                           year_html = year, output = result)

@app.route("/biofuel")
def route_biofuel():
    """
    Arguments: country (string)
    Return: inputted country by user (string) and highest biofuel 
    consumption value of that country (string)
    Purpose: Display the highest biofuel consumption for the given country
    """
    country = str(request.args['biofuel_country'])
    biofuel = route_api_biofuel(country)
    return render_template('biofuel_function.html', country_html = country, output = biofuel)

@app.route ("/data")
def route_data():
    """
    Arguments: None
    Return: returns render of data.html
    Purpose: Display data.html
    """
    return render_template('data.html')

@app.route ("/info")
def route_info():
    """
    Arguments: None
    Return: returns render of info.html
    Purpose: Display info.html
    """
    return render_template('info.html')

if __name__ == "__main__":
    app.register_blueprint(api, url_prefix='/api')
    app.run(host='0.0.0.0', port=5113)
