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

ON = "on"
OFF = "off"
LOW = "low"
PIN_LR_LOW = 10
PIN_LR_ON = 9
PIN_K = 6
PIN_TV = 11

GPIO.setwarnings(False)

client = MongoClient('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')
db = client.smartflat
lights = db.lights

PIN = int(sys.argv[1])
STATUS = int(sys.argv[2])
MANUAL = int(sys.argv[3])


GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)
GPIO.output(PIN,STATUS)


# status_str = "on"
# if STATUS==0 : 
# 	status_str = "off"

status = ON if STATUS == 1 else OFF

location_str = " "
if PIN == 11: location_str = "tv"
if PIN == 6: location_str ="kitchen"
if PIN == 9 or PIN == 10 : location_str ="livingroom"

data = {
	"location":location_str,
	"status":status,
	"manual":MANUAL,
	"date":str(datetime.datetime.utcnow()).replace(" ", "T")
}

print data
if location_str != "tv":
	db.lights.insert_one(data)

db.effectors.update_one({"$or": {"pin": PIN}, {"pinLow": PIN}, {"pinOn": PIN}}, {"$set":{"status": status}})

sys.exit()
