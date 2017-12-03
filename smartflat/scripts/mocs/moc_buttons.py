import time
import sys
import pymongo
import datetime
import os
from pymongo import MongoClient

TV = "TV"
FURNACE = "Furnace"
WINDOW = "Window"
UNKNOWN = "unknown"
ON = "on"
OFF = "off"
PIN_TV = 5
PIN_FURNACE = 13
PIN_WINDOW = 2

# get database
client = MongoClient('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')
db = client.smartflat

PIN = int(sys.argv[1])
STATUS = int(sys.argv[2])

status = OFF if STATUS == 0 else ON
db.effectors.update_one({"pin": PIN}, {"$set":{"status": status}})

location = TV if PIN == PIN_TV else FURNACE if PIN == PIN_FURNACE else UNKNOWN
date = str(datetime.datetime.utcnow()).replace(" ", "T")

button = {
  "location": location,
  "status": status,
  "manual": True,
  "date": date
}

print button
db.buttons.insert_one(button)