import RPi.GPIO as GPIO
import time
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

TRIG = 24
ECHO = 23
LED = 18
DOOR = 25

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
					
			print "He was here ",time_counter*p_time," s"
			GPIO.output(LED,GPIO.LOW)


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

print "distance measurement in progress..."
mean_distance = init(init_time, pulsating_time)
print "Distance moyenne : ",mean_distance," cm"
print "Now waiting for someone to pass by..."
waitingFor(mean_distance,pulsating_time)
GPIO.cleanup()
