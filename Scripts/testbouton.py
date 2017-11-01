import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(15,GPIO.IN)
GPIO.setup(18,GPIO.OUT)


GPIO.setup(15,GPIO.IN,pull_up_down = GPIO.PUD_UP)

while True:
	if(GPIO.input(15)==0):
		print "door opened !"
