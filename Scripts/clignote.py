import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

PINI = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(PINI,GPIO.OUT)
while True:
	GPIO.output(PINI,1)
	time.sleep(0.5)
	GPIO.output(PINI,0)
	time.sleep(0.5)


GPIO.cleanup()

