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

LIVINGROOM = "livingroom"
KITCHEN = "kitchen"
UNKNOWN = "unknown"
ON = "on"
OFF = "off"
LOW = "low"
PIN_LR_LOW = 10
PIN_LR_ON = 9
PIN_K = 6
PIN_TV = 11
PIN_FUR = 13
PIN_WIN = 2

GPIO.setwarnings(False)

client = MongoClient('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')
db = client.smartflat
lights = db.lights

PIN = int(sys.argv[1])
STATUS = int(sys.argv[2])
MANUAL = int(sys.argv[3])

if PIN != PIN_WIN and PIN != PIN_FUR:
	if PIN == PIN_LR_ON or PIN == PIN_LR_LOW :
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(PIN_LR_ON,GPIO.OUT)
		GPIO.setup(PIN_LR_LOW,GPIO.OUT)
		GPIO.cleanup()

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(PIN, GPIO.OUT)

	GPIO.output(PIN,STATUS)


status = OFF if STATUS == 0 else LOW if STATUS == 1 and PIN == PIN_LR_LOW else ON
db.effectors.update_one({"$or": [{"pin": PIN}, {"pinLow": PIN}]}, {"$set":{"status": status}})

location = KITCHEN if PIN == PIN_K else LIVINGROOM if PIN == PIN_LR_ON or PIN == PIN_LR_LOW else UNKNOWN 

data = {
	"location":location,
	"status":status,
	"manual":True if MANUAL == 1 else False,
	"date":str(datetime.datetime.utcnow()).replace(" ", "T")
}

print data
if PIN != PIN_TV and PIN != PIN_FUR and PIN != PIN_WIN:
	db.lights.insert_one(data)
else:
	db.buttons.insert_one(data)

sys.exit()
