import time
import sys
import datetime
import os
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')
db = client.smartflat
ID = ObjectId("5a19e631f36d280cc00ddb8f")

pid = os.getpid()
db.sensors.update_one({"_id": ID}, {"$set":{"status": "on", "pid": pid}}, upsert=True)

sec = 0
while True:
  data = {
    "duration":sec+1,
    "distance":10,
    "date": str(datetime.datetime.utcnow()).replace(" ", "T")
  }
  # db.ultrasonics.insert_one(data)
  time.sleep(2)
  sec += 1

