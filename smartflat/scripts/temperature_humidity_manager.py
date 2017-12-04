import datetime
import pymongo
from pymongo import MongoClient
import sys
import os

client = MongoClient('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')
db = client.smartflat

WINDOW = db.effectors.find_one({"_id": ObjectId("5a234afcf36d285138ee1b93")})["status"]
PATH = os.path.dirname(os.path.realpath(__file__))

ACTION = sys.argv[1]
MANUAL = int(sys.argv[2]) if len(sys.argv)>2 else 0

print "THERMOMETER_MANAGER : { action: "+ACTION+", manual: "+str(MANUAL)+" }"
if WINDOW in "off":
  os.system("python "+PATH+"/led_rgb_switch.py "ACTION) #switch off the rgb led (heat)

