'''			READ ME
Returns the brightness of the room as a percentage (0% = the sun is gone ; 100% = the sun paid a visit to the sensor)
It means 50 values to ignore erred data
HOW TO USE IT :
python lightsensor.py LIGHT_SENSOR_PIN

DEFAULT PIN : 26

'''
import RPi.GPIO as GPIO
import time
import sys
from pylab import log
import datetime
import pymongo
import os
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')
db = client.smartflat

ID = ObjectId("5a1f0969734d1d3ed2310a53")
db.sensors.update_one({"_id": ID}, {"$set":{"status": "on", "pid": os.getpid()}}, upsert=True)

PIN = 26

if len(sys.argv)>1:
	PIN = int(sys.argv[1])

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)
GPIO.setup(PIN, GPIO.IN)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

#MAX light = 0		100
#MIN light >1000	0
#MIN visibility >100	46

def rc_time (PIN):
    count = 0
  
    GPIO.setup(PIN, GPIO.OUT)
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(PIN, GPIO.IN)
  
    while (GPIO.input(PIN) == GPIO.LOW):
        count += 1

    return 10*(10-log(count))


cursor = db.luminosities.find().limit(1).sort([('$natural',-1)])
last_lum = 46
if cursor.count()>0:
	last_data = next(cursor,None)
	last_lum = int(last_data['luminosity'])
print last_lum

def update_data(PIN):
	global last_lum 	
	sum = 0.0
	for i in range(50):
		sum = sum + rc_time(PIN)
	sum = int(round(sum/50))
	if sum-last_lum>1 or sum-last_lum<-1:
		data = {
			'pin':PIN,
			'luminosity':sum,
			'date':str(datetime.datetime.utcnow()).replace(" ", "T")
		}
		print data
		db.luminosities.insert(data)
		# os.system("python "+PATH+"/luminosity_manager.py "+("-" if sum<last_lum else "")+sum)
		last_lum = sum

while True :
	update_data(PIN)

