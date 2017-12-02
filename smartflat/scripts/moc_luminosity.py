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
ID = ObjectId("5a1f0969734d1d3ed2310a53")

pid = os.getpid()
print pid
db.sensors.update_one({"_id": ID}, {"$set":{"status": "on", "pid": pid}}, upsert=True)

while True:
  data = {
    "luminosity":randint(1,10) / 10,
    "date": str(datetime.datetime.utcnow()).replace(" ", "T")
  }
  db.luminosities.insert_one(data)
  time.sleep(30)

