''' 			READ ME !
This script detects anyone who passes under the sensor, activator pin 
must be provided and mean distance as so

HOW TO USE IT :
python ultrasonic_start.py PIN_TO_LISTEN MEAN_DISTANCE

PIN_TO_LISTEN is the pin of the door
MEAN_DISTANCE is the mean distance calculated by the script ultrasonic_init.py
'''
import RPi.GPIO as GPIO
import time
import sys
import pymongo
import datetime
from pymongo import MongoClient

client = MongoClient('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')
db = client.smartflat
ultrasonics = db.ultrasonics


GPIO.setmode(GPIO.BCM)

TRIG = 24
ECHO = 23
DOOR = int(sys.argv[1])

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.output(TRIG, False)

GPIO.setup(DOOR,GPIO.IN,pull_up_down = GPIO.PUD_UP)

mean_distance = float(sys.argv[2])
pulsating_time = 0.01
init_time = (int)(5/pulsating_time)

data = {
	"duration":0,
	"distance":0,
	"date":0
}

def getDistance(p_time):
                GPIO.output(TRIG, True)
                time.sleep(p_time)
                GPIO.output(TRIG,False)

                while GPIO.input(ECHO)==0:
	                pulse_start = time.time()

                while GPIO.input(ECHO)==1:
                        pulse_end = time.time()
                return round( (pulse_end - pulse_start)*17150,2)


def waitingFor(mean, p_time):
	open = True
	while open :
		if GPIO.input(DOOR)==0:
			while GPIO.input(DOOR)==0:
				True
			open = not open
		distance = getDistance(p_time)
		buffer = []
		count = 1
		time_counter = 1
		if(distance<mean*0.7):
			print "Someone is detected at ",distance," cm !"
			buffer.append(distance)
			while (sum(buffer)/count<mean*0.8):
				buffer.append(getDistance(p_time))
				time_counter= time_counter + 1
				if (count<1/p_time):
					count = count+1
				else:
					del buffer[1]
			data['duration']=time_counter*p_time
			data['distance']=distance
			data['date']=datetime.datetime.utcnow()
			result = db.ultrasonics.insert_one(data)
			print result.inserted_id
			print "He was here ",time_counter*p_time," s"


def waitDoor(mean,p_time):
	open= False
	while True:
		if(GPIO.input(DOOR)==0):
			while(GPIO.input(DOOR)==0):
				True
			open = not open
			print "Door opened !"
			waitingFor(mean, p_time)
			print "Door closed !"

print "Now waiting for someone to pass by..."
waitDoor(mean_distance,pulsating_time)
GPIO.cleanup()
sys.exit
