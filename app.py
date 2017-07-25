from flask import Flask, render_template
import Adafruit_DHT  

app = Flask(__name__)

@app.route('/')
def hello(name):
	humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4) 
	return render_template('page.html', humidity=humidity, temperature=temperature)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)