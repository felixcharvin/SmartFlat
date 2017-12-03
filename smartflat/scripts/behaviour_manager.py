import datetime
import pymongo
from pymongo import MongoClient
import sys
import os

client = MongoClient('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')
db = client.smartflat

CASE = sys.argv[1]
LOCATION = sys.argv[2]
STATUS = sys.argv[3]

print "changes detected !"
print "case: "+CASE+", pin: "+LOCATION+", status:"+STATUS

def getLuminosity():
	lum = 4.6
	cursor = db.luminositites.find().limit(1).sort([('$natural',-1)])
	if cursor.count()>0:
		lum = next(cursor,None)['luminosity']
	return lum

def turn_on_livingroom(brightness):
		man = sys.argv[4] if len(sys.argv)>4 else "0"

		print brightness

		if brightness in "low" :
			os.system("python led_switch.py 10 1 " + man)
		if brightness in "high":
			os.system("python led_switch.py 9 1 " + man)
		else:
			os.system("python led_switch.py 9 0 " + man")
	

def turn_on_tv():
	os.system("python led_switch.py 11 "+sys.argv[3]+" 0")
	light_livingroom(True)
	

def light_livingroom(tv):
	lum = getLuminosity()
	if (lum<3.6 or STATUS in "1") and not tv :
		turn_on_livingroom("high")
	else:
		if lum<4.6 or STATUS in "1" :
			turn_on_livingroom("low")
		else:
			turn_on_livingroom("off")
def light_kitchen(status):
	lum = getLuminosity()
	os.system("python led_switch.py 6 "+status+" 0")
	
if CASE in "buttons":
        location = sys.argv[2]
        if location in "kitchen":
                light_kitchen(sys.argv[3])
        if location in "furnace":
                light_kitchen("1")
        if location in "livingroom":
                light_livingroom(STATUS) #HIGH OR LOW OR OFF
        if location in "tv":
                turn_on_tv()
                #exec(light_led.py 11 sys.argv[3])

        if location in "window":
                True
                #windowChanged()


if CASE in "alarm":
        status = sys.arv[2]
        if status in "on":
                True
                #switch_off_all()
                #exec(ultrasonic_init.py)
                #exec(ultrasonic_start.py mean)
        if status in "off":
                True
                ##kill process
        if status in "alert intrusion":
                True
                #alert_user()

