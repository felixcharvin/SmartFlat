import RPi.GPIO as G
import time
import threading
from threading import Thread
import sys

LED = int(sys.argv[1])
FPS = 1/24
G.setmode(G.BCM)
G.setup(LED,G.OUT)


def blink_led():
	print threading.current_thread()
	for i in range(1000000):
		G.output(LED,G.LOW)
		time.sleep(FPS)
		G.output(LED,G.HIGH)
		time.sleep(FPS)
	G.output(LED,G.LOW)



t = Thread(name="medled",target = blink_led)

t.start()
