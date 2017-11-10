import time
import sys
import pymongo
import datetime
from random import randint
from pymongo import MongoClient

client = MongoClient('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')
db = client.smartflat
lights = db.lights

for i in range(0, 20):
  hour = randint(0, 23)
  day = randint(1, 30)
  month = randint(1, 12)
  date = str(datetime.datetime(2017, month, day, hour, 0, 0))
  status = "off" if randint(0,1) == 0 else "on"
  location = "kitchen" if randint(0,1) == 0 else "livingroom"

  light = {
    "pin": randint(0,1),
    "location": location,
    "status": status,
    "manual": True,
    "date": date
  }
  print light
  result = db.lights.insert_one(light)
