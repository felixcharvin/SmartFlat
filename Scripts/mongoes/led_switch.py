'''				READ ME
Turn on or off a led
HOW TO USE IT:
python led_switch LEDS_PIN STATUS_ON_OFF MANUAL

LEDS_PIN : the pin number for the led (kitchen : 19, livingroom : 26)
STATUS_ON_OFF : 0 to turn off the led, else 1
MANUAL : 0 if automatic, else 1

'''
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

if PIN == 21: location_str ="kitchen"
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
