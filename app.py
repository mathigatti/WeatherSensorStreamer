from flask import Flask, render_template
import Adafruit_DHT  
import pandas as pd
import matplotlib.pyplot as plt

import csv

app = Flask(__name__)

def readFile(fileName):
	df = pd.read_csv(fileName, parse_dates = True, index_col = 0, skiprows=[0])
	df.head()
	return df

@app.route('/')
def index():
	humidity = readFile('sensor-values/humidity_living-room_log_2017.csv')
	temperature = readFile('sensor-values/humidity_living-room_log_2017.csv')

	humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)

    graphs = [
        dict(
            data=[
                dict(
                    x=humidity.index,  # Can use the pandas data structures directly
                    y=humidity
                )
            ],
            layout=dict(
                title='Historic Humidity'
            )
        ),
        dict(
            data=[
                dict(
                    x=temperature.index,  # Can use the pandas data structures directly
                    y=temperature
                )
            ],
            layout=dict(
                title='Historic Temperature'
            )
        )
    ]

    # Add "ids" to each of the graphs to pass up to the client
    # for templating
    ids = ['graph-{}'.format(i) for i, _ in enumerate(graphs)]

    # Convert the figures to JSON
    # PlotlyJSONEncoder appropriately converts pandas, datetime, etc
    # objects to their JSON equivalents
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

	return render_template('layouts/index.html',
                           ids=ids,
                           graphJSON=graphJSON, humidity=humidity, temperature=temperature)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
