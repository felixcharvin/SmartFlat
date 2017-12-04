import sys
import os
import time
import pymongo
import datetime
import Adafruit_DHT
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')
db = client.smartflat

ID = ObjectId("5a2313bcf36d285138ee0af1")
db.sensors.update_one({"_id": ID}, {"$set":{"status": "on", "pid": os.getpid()}}, upsert=True)

PATH = os.path.dirname(os.path.realpath(__file__))

# Parse command line parameters. if another sensor is used :
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }

sensor = Adafruit_DHT.DHT11
#DEFAULT VALUE : 3

def read_info():
	humidity, temperature = Adafruit_DHT.read_retry(sensor, PIN)
	while humidity is None or temperature is None or humidity > 100:
		humidity, temperature = Adafruit_DHT.read_retry(sensor, PIN)
	data = {
		"temperature":temperature,
		"humidity":humidity,
		"date":str(datetime.datetime.utcnow()).replace(" ", "T")
	}
	print data
	db.thermometers.insert(data)
	settings = db.sensors.find_one({"_id": ID})["settings"]
	action = "cold" if settings-temperature<-1 else "hot" if settings-temperature>1 else "normal"
	os.system("python "+PATH+"/temperature_humidity_manager.py "+action)

	return {temperature,humidity}

PIN = 3
if len(sys.argv)>1:
	PIN = sys.argv[1]

while True:
	read_info()
	time.sleep(5)
