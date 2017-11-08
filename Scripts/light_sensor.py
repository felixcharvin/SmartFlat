import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
LUM = 13

def rc_time (PIN):
	count = 0
	GPIO.setup(LUM,GPIO.OUT)
	GPIO.output(LUM,GPIO.LOW)
	time.sleep(0.1)

	while GPIO.input(LUM) == GPIO.LOW :
		count +=1
	return count

try:
	while True :
		print rc_time(LUM)
except KeyboardInterrupt:
	pass
finally:
	GPIO.cleanup()
