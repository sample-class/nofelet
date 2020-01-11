from flask import Flask, render_template
from mok_data import *

app = Flask(__name__)

@app.route('/')
def main():
    output = render_template('index.html',
                             title=title,
                             subtitle=subtitle,
                             description=description,
                             tours=tours.items())
    return output


@app.route('/from/<direction>/')
def direction(direction):
    departure = departures[direction]
    output = render_template('direction.html',
                             departures=departures.items(),
                             departure=departure,
                             direction=direction,
                             tours=tours.items())
    return output


@app.route('/tours/<id>/')
def tour(id):
    this_tour = tours[int(id)]
    output = render_template('tour.html',
                             title=this_tour['title'],
                             stars=this_tour['stars'],
                             country=this_tour['country'],
                             dep=departures[this_tour['departure']],
                             nights=this_tour['nights'],
                             picture=this_tour['picture'],
                             desc=this_tour['description'],
                             price=str(this_tour['price']))
    return output


if __name__ == '__main__':
    app.run()
