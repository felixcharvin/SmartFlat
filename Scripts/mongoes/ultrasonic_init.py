'''			READ ME
This file return the mean distance of the sensor while noone passes 
through the door

HOW TO USE IT :
python ultrasonic_init.py
'''
import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)

TRIG = 24
ECHO = 23

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.output(TRIG, False)


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
	for i in range(0,time_to_init):
		data.append(getDistance(p_time))
	return sum(data)/time_to_init


mean_distance = init(init_time, pulsating_time)
print mean_distance
GPIO.cleanup()
sys.exit
