import RPi.GPIO as GPIO
import time
import datetime
import os
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')
db = client.smartflat
ID = ObjectId("5a19e631f36d280cc00ddb8f")
PATH = os.path.dirname(os.path.realpath(__file__))

TRIG = 24
ECHO = 23
LED = 18

#cleanup before start
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)
GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.output(TRIG, False)

GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED,GPIO.LOW)

mean_distance = 0
pulsating_time = 0.01
init_time = (int)(5/pulsating_time)

def getDistance(p_time):
	GPIO.output(TRIG, True)
	time.sleep(p_time)
	GPIO.output(TRIG,False)

	while GPIO.input(ECHO)==0:
		pulse_start = time.time()

	while GPIO.input(ECHO)==1:
					pulse_end = time.time()
	return round( (pulse_end - pulse_start)*17150,2)


def init(time_to_init, p_time):
	data = []
	print "Waiting for sensor to settle..."
	for i in range(0,time_to_init):
		data.append(getDistance(p_time))
	return sum(data)/time_to_init

def updateDB(time, distance):
	data = {
		"distance": distance,
		"duration": time,
		"date": str(datetime.datetime.utcnow()).replace(" ", "T")
	}
	db.ultrasonics.insert_one(data)
	db.sensors.update_one({"_id": ID}, {"$set":{"alert": True}})
	os.system("python "+PATH+"/sensors_manager.py alarm alert")

def waitingFor(mean, p_time):
	while True :
		distance = getDistance(p_time)
		buffer = []
		count = 1
		time_counter = 1
		if(distance<mean*0.7):
			GPIO.output(LED,GPIO.HIGH)
			buffer.append(distance)
			while (sum(buffer)/count<mean*0.8):
				buffer.append(getDistance(p_time))
				time_counter= time_counter + 1
				if (count<1/p_time):
					count = count+1
				else:
					del buffer[1]
			
			time = time_counter*p_time
			if time > 1:
				updateDB(time, distance)
			GPIO.output(LED,GPIO.LOW)

print "distance measurement in progress..."
mean_distance = init(init_time, pulsating_time)
print "Mean distance : ",mean_distance," cm"

db.sensors.update_one({"_id": ID}, {"$set":{"status": "on", "alert": False, "pid": os.getpid()}}, upsert=True)

print "Now waiting for someone to pass by..."
waitingFor(mean_distance,pulsating_time)
GPIO.cleanup()
