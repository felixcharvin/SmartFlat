import time
import sys
import datetime
import os
import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')
db = client.smartflat

pid = os.getpid()
print pid

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

sys.exit