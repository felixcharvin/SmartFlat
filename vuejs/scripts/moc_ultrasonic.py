import time
import sys
import pymongo
import datetime

from pymongo import MongoClient

client = MongoClient('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')
db = client.smartflat
ultrasonics = db.ultrasonics

sec = 0
while sec != 10:
  data = {
    "duration":sec+1,
    "distance":10,
    "date":datetime.datetime.utcnow()
  }
  result = db.ultrasonics.insert_one(data)
  print result.inserted_id
  time.sleep(2)
  sec += 1

sys.exit