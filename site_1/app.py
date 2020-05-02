from flask import Flask, render_template


from site_data import title, subtitle, description, departures, tours



app = Flask(__name__)


@app.route('/')  # route for main page
def render_main():
    return render_template('index.html', title=title, subtitle=subtitle, description=description, departures=departures)


@app.route('/departures/')
def render_departures():
    return render_template('departure.html')


@app.route('/tours/')
def render_tours():
    return render_template('departure.html')


@app.route('/departures/<departure>/')
def render_departure_page(departure):
    return 'здесь будет направление ' + departure


@app.route('/tours/<int:id>/')
def render_tour_page(id):
    #
    return 'здесь будет тур' + str(id)

app.run('0.0.0.0', 8000, debug=True)
