from flask import Flask, render_template
import sys
sys.path.append('/Users/minhlynguyen/Documents/software-engineering/git/ridemate/RideMate')
import config
import time
import requests
import json

app = Flask(__name__)


@app.route('/')

@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/station')
def station_page():
    return render_template('station.html')


LATITUDE = 53.340927
LONGITUDE = -6.262501
r = requests.get(config.WEATHER_URL,params={"latitude":LATITUDE,"longitude":LONGITUDE,"hourly":config.HOURLY,
        "daily":config.DAILY,"current_weather":"true","timeformat":"unixtime","timezone":config.TIMEZONE})
weather = json.loads(r.text)

@app.route('/station/<int:station_id>')
def station(station_id):
    return f'Retrieving info for Station: {station_id}'.format(station_id)

@app.route('/weather')
def weather():
    LATITUDE = 53.340927
    LONGITUDE = -6.262501
    r = requests.get(config.WEATHER_URL,params={"latitude":LATITUDE,"longitude":LONGITUDE,"hourly":config.HOURLY,
    "daily":config.DAILY,"current_weather":"true","timeformat":"unixtime","timezone":config.TIMEZONE})
    weather = json.loads(r.text)
    return f'Weather information: {weather}'.format(weather)

@app.route('/about/<username>')
def about_page(username):
    return f'<h1>this is the about page of {username}</h1>'

if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=4444, debug=True)

# Testing decorators:
def build_regression_model(**kwargs):
    print('building model...')

# build_regression_model()

start = time.time()
build_regression_model()
end = time.time()

print(end-start)
print("took: {} secs".format(end-start))

def timeit(method):
    def timed(*args,**kw):
        start = time.time()
        result = method(*args,**kw)
        end = time.time()
        print("")

