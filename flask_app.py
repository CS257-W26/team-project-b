'''
The eventual location for the Flask app interface for the project.
'''
import base64
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from flask import Flask, render_template, request
from ProductionCode.core import Features
from flask_api import (route_api_average, route_api_ratio,
route_api_year_co2, route_api_year_energy, route_api_biofuel, api, route_api_graph)

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

@app.route ("/graph")
def route_graph():
    """
    Arguments: None
    Return: returns render of data.html
    Purpose: Display data.html
    """
    country = str(request.args['graph_country'])
    graph_data = route_api_graph(country)

    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title(f'{country} CO2')
    axis.set_xlabel("Years")
    axis.set_ylabel("CO2")
    axis.locator_params(nbins=10)

    axis.plot(graph_data[0], graph_data[1])
    co2_png_image = io.BytesIO()
    FigureCanvas(fig).print_png(co2_png_image)
    # Encode PNG image to base64 string
    co2_graph = "data:image/co2_png;base64,"
    co2_graph += base64.b64encode(co2_png_image.getvalue()).decode('utf8')

    axis.plot = fig.clf()
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title(f'{country} Energy')
    axis.set_xlabel("Years")
    axis.set_ylabel("Energy")
    axis.locator_params(nbins=10)
    axis.plot(graph_data[2], graph_data[3])
    energy_png_image = io.BytesIO()
    FigureCanvas(fig).print_png(energy_png_image)
    energy_graph = "data:image/energy_png;base64,"
    energy_graph += base64.b64encode(energy_png_image.getvalue()).decode('utf8')
    return render_template("graph.html", co2Image=co2_graph, energyImage=energy_graph)

if __name__ == "__main__":
    app.register_blueprint(api, url_prefix='/api')
    app.run(host='0.0.0.0', port=5113)
