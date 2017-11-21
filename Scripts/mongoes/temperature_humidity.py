import sys

import Adafruit_DHT


# Parse command line parameters.
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }

sensor = Adafruit_DHT.DHT11
pin = sys.argv[1]
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
for i in range(0,5):
	hum, temp = Adafruit_DHT.read_retry(sensor, pin)
	while hum is None or temp is None:
		hum, temp = Adafruit_DHT.read_retry(sensor, pin)
	temperature = temperature + temp
	humidity = humidity + hum

print('{0:0.1f}*  {1:0.1f}%'.format(temperature/float(5), humidity/float(5)))
