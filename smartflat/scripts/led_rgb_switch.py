import RPi.GPIO as G
import time
import random
import sys

RED = 22
GREEN = 27
BLUE = 17
FPS = 1/24

G.setmode(G.BCM)
G.setup(RED,G.OUT)
G.setup(GREEN,G.OUT)
G.setup(BLUE,G.OUT)

red = 0
green = 0
blue = 0

STATUS = sys.argv[1] if len(sys.argv)>1 else ""

if STATUS == "cold":
  blue = 1
elif STATUS == "hot":
  red = 1
elif STATUS == "normal":
  red = 1
  green = 1
  blue = 1

G.output(RED,red)
G.output(GREEN,green)
G.output(BLUE,blue)

