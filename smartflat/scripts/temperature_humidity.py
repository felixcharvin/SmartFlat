import sys
import time
import pymongo
import datetime
from pymongo import MongoClient
import Adafruit_DHT


client = MongoClient('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')
db = client.smartflat
temphum = db.thermometers


# Parse command line parameters. if another sensor is used :
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
	data = {
		"temperature":temperature,
		"humidity":humidity,
		"date":str(datetime.datetime.utcnow()).replace(" ", "T")
	}
	db.thermometers.insert(data)
	return {temperature,humidity}


while True:
	read_info()
	time.sleep(5)
