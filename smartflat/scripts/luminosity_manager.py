import datetime
import pymongo
import sys
import os
from pymongo import MongoClient
from bson.objectid import ObjectId

PIN_LR = 9
PIN_LR_LOW = 10
PIN_TV = 11

client = MongoClient('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')
db = client.smartflat

PATH = os.path.dirname(os.path.realpath(__file__))
TV = db.effectors.find_one({"pin": PIN_TV})["status"]
LR = db.effectors.find_one({"pin": PIN_LR})["status"]
ALARM = db.sensors.find_one({"_id": ObjectId("5a19e631f36d280cc00ddb8f")})["status"]

LUMINOSITY = int(sys.argv[1])
MANUAL = int(sys.argv[2]) if len(sys.argv)>2 else 0

print "LUMINOSITY_MANAGER : { lum: "+str(LUMINOSITY)+", manual: "+str(MANUAL)+" }"
if LUMINOSITY < 46 and LR in "off" and ALARM in "off":
  os.system("python "+PATH+"/led_switch.py "+(str(PIN_LR_LOW) if TV in "on" else str(PIN_LR))+" 1 "+str(MANUAL))

