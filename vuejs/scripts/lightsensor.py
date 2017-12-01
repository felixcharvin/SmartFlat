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

PIN = 19

if len(sys.argv)>1:
	PIN = int(sys.argv[1])

GPIO.setmode(GPIO.BCM)

#MAX light = 0		10
#MIN light >1000	0
#MIN visibility >100	4,6

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
last = # TODO retrieve data from db

def update_data(PIN):
	
	sum = 0.0
	for i in range(50):
		sum = sum + rc_time(PIN)
	if sum-last>0.01 || sum-last<0.01:
		


