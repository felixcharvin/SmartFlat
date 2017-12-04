import RPi.GPIO as GPIO
import time
import os

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

client = MongoClient('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')
db = client.smartflat

TRIG = 24
ECHO = 23
LED = 18

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.output(TRIG, False)

GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED,GPIO.LOW)

GPIO.setup(DOOR,GPIO.IN,pull_up_down = GPIO.PUD_UP)

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
			print "He was here ",time," s"
			if time > 1:
				
			GPIO.output(LED,GPIO.LOW)

print "distance measurement in progress..."
mean_distance = init(init_time, pulsating_time)
print "Mean distance : ",mean_distance," cm"

ID = ObjectId("5a19e631f36d280cc00ddb8f")
pid = os.getpid()
print pid
db.sensors.update_one({"_id": ID}, {"$set":{"status": "on", "pid": pid}}, upsert=True)

print "Now waiting for someone to pass by..."
waitingFor(mean_distance,pulsating_time)
GPIO.cleanup()
