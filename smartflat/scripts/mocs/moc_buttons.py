import time
import sys
import pymongo
import datetime
from pymongo import MongoClient

TV = "TV"
FURNACE = "Furnace"
UNKNOWN = "unknown"
ON = "on"
OFF = "off"
PIN_TV = 5
PIN_FURNACE = 13
PIN_WINDOW = 2

pin = int(sys.argv[1])
stat = int(sys.argv[2])

status = OFF if stat == 0 else ON
location = TV if pin == PIN_TV else FURNACE if pin == PIN_FURNACE else UNKNOWN
date = str(datetime.datetime.utcnow()).replace(" ", "T")

button = {
  "pin": pin,
  "location": location,
  "status": status,
  "manual": True,
  "date": date
}

print button
db.buttons.insert_one(button)
db.effectors.update_one({"pin": pin}, {"$set":{"status": status}})