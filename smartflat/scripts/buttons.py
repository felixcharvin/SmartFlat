import RPi.GPIO as GPIO
import time
import sys
import os
import pymongo
import datetime
from pymongo import MongoClient

client = MongoClient('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')
db = client.smartflat
PATH = os.path.dirname(os.path.realpath(__file__))

PIN_WIN = 2
PIN_LR = 4
PIN_TV = 5
PIN_K = 19
PIN_FUR = 13
ON = "on"
OFF = "off"

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_WIN, GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(PIN_LR, GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(PIN_TV, GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(PIN_K, GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(PIN_FUR, GPIO.IN,pull_up_down = GPIO.PUD_UP)

# TODO led_switch already manages low and on

def fill_data(pin):
	effector = db.effectors.find_one({"btn": pin})
	print effector
	status = OFF if effector['status'] == ON else ON

	data = {
		'location':effector["location"],
		'status':status,
		'manual':True,
		'date':str(datetime.datetime.utcnow()).replace(" ", "T")
	}
	print data
	db.buttons.insert(data)
	db.effectors.update_one({"btn": pin}, {"$set":{"status": status}})
	# os.system("python behaviour_manager.py buttons "+loc+" "+("0" if status == OFF else "1")+" 1")
	os.system("python "+PATH+"/buttons_manager.py "+str(effector["pin"])+" "+("0" if status == OFF else "1")+" 1")

while True:
	if GPIO.input(PIN_WIN)==0:
		while GPIO.input(PIN_WIN)==0:
			True
		#print "PIN_WIN !"
		fill_data(PIN_WIN)
	
	if GPIO.input(PIN_LR)==0:
		while GPIO.input(PIN_LR)==0:
			True
		#print "Living room !"
		fill_data(PIN_LR)
	if GPIO.input(PIN_TV)==0:
		while GPIO.input(PIN_TV)==0:
			True
		#print "PINS_TVvision !"
		fill_data(PIN_TV)
	if GPIO.input(PIN_K)==0:
		while GPIO.input(PIN_K)==0:
			True
		#print "Kitchen !"
		fill_data(PIN_K)
	if GPIO.input(PIN_FUR)==0:
		while GPIO.input(PIN_FUR)==0:
			True
		#print "Furnace !"
		fill_data(PIN_FUR)
