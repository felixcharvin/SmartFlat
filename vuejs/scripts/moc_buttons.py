import time
import sys
import pymongo
import datetime
from pymongo import MongoClient

client = MongoClient('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')
db = client.smartflat
buttons = db.buttons

pin = sys.argv[1]
stat = sys.argv[2]

status = "off" if stat == "0" else "on"
location = "TV" if pin == "0" else "Door"
date = str(datetime.datetime.utcnow())

button = {
  "pin": pin,
  "location": location,
  "status": status,
  "manual": True,
  "date": date
}

print button
result = db.buttons.insert_one(light)
