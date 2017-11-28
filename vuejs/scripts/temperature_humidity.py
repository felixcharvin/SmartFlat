import sys
import time

import Adafruit_DHT


# Parse command line parameters.
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }

sensor = Adafruit_DHT.DHT11
#DEFAULT VALUE : 3
PIN = 3
if len(sys.argv)>1:
	PIN = sys.argv[1]
def read_info():
	humidity, temperature = Adafruit_DHT.read_retry(sensor, PIN)
	while humidity is None or temperature is None or humidity > 100:
		humidity, temperature = Adafruit_DHT.read_retry(sensor, PIN)
	return {temperature,humidity}

while True:
	print read_info()
	time.sleep(5)
