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

# get database
client = MongoClient('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')
db = client.smartflat

# get arguments
pin = int(sys.argv[1])
stat = int(sys.argv[2])

location = KITCHEN if pin == 0 else LIVINGROOM if pin == 1 else UNKNOWN
status = OFF if stat == 0 else LOW if stat == 2 and location == LIVINGROOM else ON
date = str(datetime.datetime.utcnow()).replace(" ", "T")

light = {
  "pin": pin,
  "location": location,
  "status": status,
  "manual": True,
  "date": date
}

print light
db.lights.insert_one(light)
db.effectors.update_one({"pin": pin}, {"$set":{"status": status}})