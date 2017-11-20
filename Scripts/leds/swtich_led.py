import RPi.GPIO as G
import sys

PIN = int(sys.argv[1])
MODE = int(sys.argv[2])

G.setmode(G.BCM)
G.setup(PIN,G.OUT)
G.output(PIN,MODE)	
if MODE == 0:
	G.cleanup()
