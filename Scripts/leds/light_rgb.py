import RPi.GPIO as G
import time
import random

RED = 22
GREEN = 27
BLUE = 17
FPS = 1/24

G.setmode(G.BCM)
G.setup(RED,G.OUT)
G.setup(GREEN,G.OUT)
G.setup(BLUE,G.OUT)
import sys

red =   int(sys.argv[1])
green = int(sys.argv[2])
blue =  int(sys.argv[3])

G.output(RED,red)
G.output(GREEN,green)
G.output(BLUE,blue)

