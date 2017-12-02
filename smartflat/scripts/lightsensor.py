'''			READ ME
Returns the brightness of the room as a percentage (0% = the sun is gone ; 100% = the sun paid a visit to the sensor)
It means 50 values to ignore erred data
HOW TO USE IT :
python lightsensor.py LIGHT_SENSOR_PIN

DEFAULT PIN : 19

'''
import RPi.GPIO as GPIO
import time
import sys
from pylab import log
import datetime
import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')
db = client.smartflat



PIN = 19

if len(sys.argv)>1:
	PIN = int(sys.argv[1])

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


data = {
	'pin':PIN,
	'luminosity':0,
	'date':str(datetime.datetime.utcnow())
}
cursor = db.luminosities.find().limit(1).sort([('$natural',-1)])
last_lum = 4.6
if cursor.count()>0:
	last_data = next(cursor,None)
	last_lum = last_data['luminosity']

def update_data(PIN):
	global last_lum 	
	sum = 0.0
	for i in range(50):
		sum = sum + rc_time(PIN)
	sum = sum/50.0
	if sum-last_lum>1 or sum-last_lum<-1:
		data = {
			'pin':PIN,
			'luminosity':sum,
			'date':str(datetime.datetime.utcnow())
		}
		result = db.luminosities.insert(data)
		last_lum = sum

while True :
	update_data(PIN)

