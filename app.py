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

def saveFig(df, imgName):
	plt.cla() # descarto datos
	df.plot()
	plt.savefig(imgName+".png")

@app.route('/')
def index():
	humidity = readFile('sensor-values/humidity_living-room_log_2017.csv')
	temperature = readFile('sensor-values/humidity_living-room_log_2017.csv')
	saveFig(humidity, "humedadIMG")
	saveFig(temperature, "temperaturaIMG")
	humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)
	return render_template('page.html', humidity=humidity, temperature=temperature)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
