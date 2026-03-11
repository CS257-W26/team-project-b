'''
The eventual location for the Flask app interface for the project.
'''
from flask import Flask, render_template, request
from ProductionCode.core import Features
from flask_api import (route_api_average, route_api_ratio,
route_api_year_co2, route_api_year_energy, route_api_biofuel, route_api_graph, api)

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


@app.route("/stats")
def route_country_stats():
    '''
    Purpose: Handles user input in the homepage
    '''
    country = str(request.args['country_stats'])
    try:
        average = route_api_average(country)
        ratio = route_api_ratio(country)
        biofuel = route_api_biofuel(country)
    except ValueError:
        return render_template('na.html', country_html = country)

    return render_template('stats.html', function = "stats",
                           country_html = country,
                           average_html = average,
                           ratio_html = ratio,
                           biofuel_html = biofuel)

@app.route("/year_co2")
def route_year_co2():
    '''Arguments: year (string)
    Return: A list of lists (string) with each country and
    total CO2 emissions from a specific year
    Purpose: To display the total CO2 emissions of each country
    in the dataset from a specific year
    '''
    year = str(request.args['year_co2'])
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
    year = str(request.args['year_energy'])
    result = route_api_year_energy(year)
    return render_template('year_energy_function.html', title = 'Year Energy',
                           year_html = year, output = result)

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
