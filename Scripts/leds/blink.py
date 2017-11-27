import RPi.GPIO as G
import time
import sys

LED = int(sys.argv[1])
INTENSITY = float(sys.argv[2])
TIME = -1
if len(sys.argv)>3: 
	TIME = sys.argv[3]

FPS = 1.0/(24.0*INTENSITY)

G.setmode(G.BCM)
G.setup(LED, G.OUT)
G.output(LED,G.LOW)


while True : 
	G.output(LED,G.HIGH)
	time.sleep(FPS)
	G.output(LED,G.LOW)
	time.sleep(FPS)
G.cleanup()
