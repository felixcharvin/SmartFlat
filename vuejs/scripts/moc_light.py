import time
import sys
import pymongo
import datetime
from pymongo import MongoClient

client = MongoClient('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')
db = client.smartflat
lights = db.lights

pin = sys.argv[1]
stat = sys.argv[2]

status = "off" if stat == "0" else "on"
location = "kitchen" if pin == "0" else "livingroom"

light = {
  "pin": pin,
  "location": location,
  "status": status,
  "manual": True,
  "date": datetime.datetime.utcnow()
}

print light
result = db.lights.insert_one(light)
print result.inserted_id

sys.exit