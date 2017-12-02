import time
import sys
import pymongo
import datetime
from random import randint
from pymongo import MongoClient

LIVINGROOM = "livingroom"
KITCHEN = "kitchen"
ON = "on"
OFF = "off"
LOW = "low"

client = MongoClient('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')
db = client.smartflat
lights = db.lights
lightsList = []

count = sys.argv[1]
for i in range(0, int(count)):
  hour = randint(0, 23)
  day = randint(1, 30)
  month = randint(1, 12)
  date = str(datetime.datetime(2017, month, day, hour, 0, 0)).replace(" ", "T")
  stat = randint(0,2)
  location = KITCHEN if randint(0,1) == 0 else LIVINGROOM
  status = OFF if stat == 0 else LOW if stat == 2 and location == LIVINGROOM else ON

  light = {
    "location": location,
    "status": status,
    "manual": True,
    "date": date
  }
  print light
  lightsList.append(light)

result = db.lights.insert_many(lightsList)