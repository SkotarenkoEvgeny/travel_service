from flask import Flask, render_template
import random

from site_data import title, subtitle, description, departures, tours



app = Flask(__name__)


@app.route('/')  # route for main page
def render_main():
    random_hotel_list = {i: tours[i] for i in random.sample(list(tours), 6)}
    return render_template('index.html', title=title, subtitle=subtitle, description=description,
                           departures=departures, RHL=random_hotel_list)


@app.route('/departures/<departure>/')
def render_departures_page(departure):
    # create a hotel list with current departure
    hotel_list = []
    for i in tours.keys():
        if tours[i]['departure'] == departure:
            raw_data = tours[i]
            raw_data.update({'id': i})
            hotel_list.append(raw_data)
    departure = departures[departure]
    return render_template('departure.html', departures=departures, hotel_list=hotel_list, departure=departure)


@app.route('/tours/<int:id>/')
def render_tour_page(id):
    tour = tours.get(id, None)
    if tour is None:
        # added the departures key in hope, that will be fix this bug in next course steps
        return render_template('bad_data.html', departures=departures)
    else:
        # added the departures key in hope, that will be fix this bug in next course steps
        return render_template('tour.html', tour=tour, departures=departures)


@app.route('/pay/<int:price>/')
def render_pay_page(price):
    return render_template('pay_management.html', price=price, departures=departures)

app.run('0.0.0.0', 8000, debug=True)
