import RPi.GPIO as GPIO
import time
import sys
import datetime
from pymongo import MongoClient

# Give 3 params when using this file : 
# python light_led.py PIN STATUS MANUAL_OR_AUTO
# exemple :
# python light_led.py 18 1 0
# which means the AI turns on the light in the kitchen

client = MongoClient('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smasmartflat')
db = client.smartflat
lights = db.lights

PIN = int(sys.argv[1])
STATE = int(sys.argv[2])
MANUAL = int(sys.argv[3])

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN,GPIO.OUT)
GPIO.output(PIN,STATE)
location = "kitchen" if PIN == 18 else "livingroom"

light = {
  "pin": PIN,
   "location": location,
  "status": STATE,
  "manual": MANUAL==1,
  "date": datetime.datetime.utcnow()
}

print light
result = db.lights.insert_one(light)
print result.inserted_id
sys.exit()
