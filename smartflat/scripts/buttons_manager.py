import datetime
import pymongo
from pymongo import MongoClient
import sys
import os

client = MongoClient('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')
db = client.smartflat

PIN_WIN = 1000
PIN_LR = 9
PIN_TV = 11
PIN_K = 6
PIN_FUR = 999

PIN = int(sys.argv[1])
LOCATION = sys.argv[2]
STATUS = int(sys.argv[3])
MANUAL = int(sys.argv[4]) if len(argv)>4 else 0

print "BTN AI changes detected !"
print "pin: "+PIN+", location: " + LOCATION + ", status: "+STATUS

def getLuminosity():
	lum = 4.6
	cursor = db.luminositites.find().limit(1).sort([('$natural',-1)])
	if cursor.count()>0:
		lum = next(cursor,None)['luminosity']
	return lum

def switch_on_lr(brightness):
  print brightness

  if brightness in "low" :
    os.system("python led_switch.py 10 1 " + MANUAL)
  if brightness in "on":
    os.system("python led_switch.py 9 1 " + MANUAL)
  else:
    os.system("python led_switch.py 9 0 " + MANUAL")
		

def light_livingroom(tv):
	lum = getLuminosity()
	if (lum<3.6 or STATUS in "1") and not tv :
		switch_on_lr("on")
	else:
		if lum<4.6 or STATUS in "1":
			switch_on_lr("low")
		else:
			switch_on_lr("off")
	

if PIN in PIN_K or PIN in PIN_FUR:
	os.system("python led_switch.py "+PIN+" "+STATUS+" "+MANUAL)
if PIN in PIN_LR:
  light_livingroom(False)
if PIN in PIN_TV:
	os.system("python led_switch.py "+PIN_TV+" "+STATUS+" "+MANUAL)
	light_livingroom(True)
if PIN in PIN_WIN:
  print "todo"
