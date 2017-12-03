import datetime
import pymongo
from pymongo import MongoClient
import sys
import os

client = MongoClient('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')
db = client.smartflat

PIN_WIN = 2
PIN_LR = 9
PIN_TV = 11
PIN_K = 6
PIN_FUR = 13
PATH = os.getcwd()

print PATH

PIN = int(sys.argv[1])
STATUS = int(sys.argv[2])
MANUAL = int(sys.argv[3]) if len(sys.argv)>3 else 0

print "pin: "+str(PIN)+", status: "+str(STATUS)+", manual: "+str(MANUAL)

def getLuminosity():
	lum = 4.6
	cursor = db.luminositites.find().limit(1).sort([('$natural',-1)])
	if cursor.count()>0:
		lum = next(cursor,None)['luminosity']
	return lum

def switch_on_lr(brightness):
  print brightness

  if brightness in "low" :
    os.system("python "+PATH+"/scripts/led_switch.py 10 1 " + str(MANUAL))
  elif brightness in "on":
    os.system("python "+PATH+"/scripts/led_switch.py 9 1 " + str(MANUAL))
  else:
    os.system("python "+PATH+"/scripts/led_switch.py 9 0 " + str(MANUAL))
		

def light_livingroom(tv):
	lum = getLuminosity()
	if (lum<3.6 or STATUS == 1) and not tv :
		switch_on_lr("on")
	elif lum<4.6 or STATUS == 1:
		switch_on_lr("low")
	else:
		switch_on_lr("off")
	

if PIN == PIN_K or PIN == PIN_FUR:
	os.system("python "+PATH+"/scripts/led_switch.py "+str(PIN_K)+" "+str(STATUS)+" "+str(MANUAL))
if PIN == PIN_LR:
  light_livingroom(False)
if PIN == PIN_TV:
	os.system("python "+PATH+"/scripts/led_switch.py "+str(PIN_TV)+" "+str(STATUS)+" "+str(MANUAL))
	if STATUS==1: light_livingroom(True)
if PIN == PIN_WIN:
	os.system("python "+PATH+"/scripts/led_rgb_switch.py") #switch off the rgb led (heat)
