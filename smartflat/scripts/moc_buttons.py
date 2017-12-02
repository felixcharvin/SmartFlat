import time
import sys
import pymongo
import datetime
from pymongo import MongoClient

TV = "TV"
FURNACE = "Furnace"
WINDOW = "Window"
UNKNOWN = "unknown"
ON = "on"
OFF = "off"
PIN_TV = 20
PIN_FURNACE = 8
PIN_WINDOW = 10

# get database
client = MongoClient('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')
db = client.smartflat

pin = int(sys.argv[1])
stat = int(sys.argv[2])

status = OFF if stat == 0 else ON
location = TV if pin == PIN_TV else FURNACE if pin == PIN_FURNACE else WINDOW if pin == PIN_WINDOW else UNKNOWN
date = str(datetime.datetime.utcnow()).replace(" ", "T")

button = {
  "location": location,
  "status": status,
  "manual": True,
  "date": date
}

print button
db.buttons.insert_one(button)
db.effectors.update_one({"pin": pin}, {"$set":{"status": status}})
