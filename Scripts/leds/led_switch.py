import RPi.GPIO as GPIO
import sys
import pymongo
import datetime
from pymongo import MongoClient

GPIO.setwarnings(False)

client = MongoClient('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')
db = client.smartflat
lights = db.lights

PIN = int(sys.argv[1])
STATUS = int(sys.argv[2])
MANUAL = int(sys.argv[3])==1


GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)
GPIO.output(PIN,STATUS)


status_str = "on"
if STATUS==0 : 
	status_str = "off"

location_str = " "

if PIN == 19: location_str ="kitchen"
if PIN == 26: location_str ="livingroom"

data = {
	"pin":sys.argv[1],
	"location":location_str,
	"status":status_str,
	"manual":MANUAL,
	"date":datetime.datetime.utcnow()
}

print data
result = db.lights.insert_one(data)
print result.inserted_id

sys.exit()
