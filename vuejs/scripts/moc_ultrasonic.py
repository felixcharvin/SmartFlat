import time
import sys
import datetime
import os
import pymongo
from random import randint
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')
db = client.smartflat
ID = ObjectId("5a19e631f36d280cc00ddb8f")

pid = os.getpid()
print pid
db.sensors.update_one({"_id": ID}, {"$set":{"status": "on", "pid": pid}}, upsert=True)

while True:
  data = {
    "duration":randint(1,9),
    "distance":10,
    "date": str(datetime.datetime.utcnow()).replace(" ", "T")
  }
  db.ultrasonics.insert_one(data)
  time.sleep(2)

