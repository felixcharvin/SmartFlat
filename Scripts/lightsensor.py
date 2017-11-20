import RPi.GPIO as GPIO
import time
import sys
from pylab import log

PIN = int(sys.argv[1])

GPIO.setmode(GPIO.BCM)

#MAX light = 0		10
#MIN light >1000	0
#MIN visibility >100	4,6

def rc_time (PIN):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(PIN, GPIO.OUT)
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(PIN, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(PIN) == GPIO.LOW):
        count += 1

    return 10*(10-log(count))

#Catch when script is interrupted, cleanup correctly
try:
    # Main loop
    while True:
        print rc_time(PIN)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
