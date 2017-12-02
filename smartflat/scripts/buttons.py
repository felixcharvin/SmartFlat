import RPi.GPIO as GPIO
import time
import sys
import pymongo
import datetime
from pymongo import MongoClient

client = MongoClient('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')
db = client.smartflat
buttons = db.buttons

WINDOW = 2
LIVRO = 4
TELE = 5
KIT = 19
FUR = 13

data = {
	"pin":0,
	"location":0,
	"status":0,
	"manual":True,
	"date":str(datetime.datetime.utcnow())
}

GPIO.setmode(GPIO.BCM)
GPIO.setup(WINDOW, GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(LIVRO, GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(TELE, GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(KIT, GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(FUR, GPIO.IN,pull_up_down = GPIO.PUD_UP)

def fill_data(pin,loc):
	last = db.buttons.find({'location':loc}).limit(1).sort([('$natural',-1)])
	status = 1
	if last.count()>0:
		old =  next(last,None)
		print old
		status = old['status']
	data['pin']=str(pin)
	data['location']=loc
	data['status']=str(not status)
	data['date']=str(datetime.datetime.utcnow())
	result = db.buttons.insert(data)
	print data
	print result


#fill_data(WINDOW,'window')

while True:
	if GPIO.input(WINDOW)==0:
		while GPIO.input(WINDOW)==0:
			True
		print "Window !"
		fill_data(WINDOW,'window')
	if GPIO.input(LIVRO)==0:
		while GPIO.input(LIVRO)==0:
			True
		print "Living room !"
		fill_data(LIVRO,'living room')
	if GPIO.input(TELE)==0:
		while GPIO.input(TELE)==0:
			True
		print "Television !"
		fill_data(TELE,'tv')
	if GPIO.input(KIT)==0:
		while GPIO.input(KIT)==0:
			True
		print "Kitchen !"
		fill_data(KIT,'kitchen')
	if GPIO.input(FUR)==0:
		while GPIO.input(FUR)==0:
			True
		print "Furnace !"
		fill_data(FUR,'furnace')
