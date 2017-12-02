import sys
import pymongo
import datetime
from pymongo import MongoClient

# define const
LIVINGROOM = "livingroom"
KITCHEN = "kitchen"
UNKNOWN = "unknown"
ON = "on"
OFF = "off"
LOW = "low"
PIN_LR_LOW = 10
PIN_LR_ON = 9
PIN_K = 6

# get database
client = MongoClient('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')
db = client.smartflat

# get arguments
pin = int(sys.argv[1])
stat = int(sys.argv[2])
manual = int(sys.argv[3])

status = OFF if stat == 0 else LOW if stat == 2 and location == LIVINGROOM else ON
db.effectors.update_one({"pin": pin}, {"$set":{"status": status}})

location = KITCHEN if pin == PIN_K else LIVINGROOM if pin == PIN_LR_LOW or pin == PIN_LR_ON else UNKNOWN
date = str(datetime.datetime.utcnow()).replace(" ", "T")

light = {
  "pin": pin,
  "location": location,
  "status": status,
  "manual": manual,
  "date": date
}

print light
db.lights.insert_one(light)