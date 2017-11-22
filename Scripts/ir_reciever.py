import RPi.GPIO as GPIO
import sys
import time

EAR = int(sys.argv[1])

GPIO.setmode(GPIO.BCM)
GPIO.setup(EAR,GPIO.IN)

while True:
	print GPIO.input(EAR)
	time.sleep(1)
