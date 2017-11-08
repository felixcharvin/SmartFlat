import RPi.GPIO as GPIO
import time
import sys

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
