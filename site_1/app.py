from flask import Flask, render_template
import random

from site_data import title, subtitle, description, departures, tours



app = Flask(__name__)


@app.route('/')  # route for main page
def render_main():
    return render_template('index.html', title=title, subtitle=subtitle, description=description,
                           departures=departures)


@app.route('/departures/<departure>/')
def render_departures_page(departure):
    tours_list = {i:tours[i]  for i in random.sample(list(tours), 3)}
    return render_template('departure.html', departures=departures, tours_list=tours_list)


@app.route('/tours/<int:id>/')
def render_tour_page(id):
    tour = tours.get(id, None)
    if tour is None:
        # added the departures key in hope, that will be fix this bug in next course steps
        return render_template('bad_data.html', departures=departures)
    else:
        # added the departures key in hope, that will be fix this bug in next course steps
        return render_template('tour.html', tour=tour, departures=departures)

app.run('0.0.0.0', 8000, debug=True)
