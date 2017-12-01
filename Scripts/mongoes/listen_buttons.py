import RPi.GPIO as GPIO
import time
import sys
import pymongo
import datetime
from pymongo import MongoClient

client = MongoClient('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')
db = client.smartflat
buttons = db.buttons

DOOR=25
#WINDOW
#


status = {
	"door":1,
	"tv":1,
	"furnace":1
}


door = {
	"pin":25,
	"location":"Door",
	"status":stats['door'],
	"manual":True,
	"date":0
}



