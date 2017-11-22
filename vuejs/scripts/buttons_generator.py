import time
import sys
import pymongo
import datetime
from random import randint
from pymongo import MongoClient

client = MongoClient('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')
db = client.smartflat
buttons = db.buttons
buttonsList = []

count = sys.argv[1]
for i in range(0, int(count)):
  hour = randint(0, 23)
  day = randint(1, 30)
  month = randint(1, 12)
  date = str(datetime.datetime(2017, month, day, hour, 0, 0)).replace(" ", "T")
  status = "off" if randint(0,1) == 0 else "on"
  location = "TV" if randint(0,1) == 0 else "Door"

  button = {
    "pin": randint(0,1),
    "location": location,
    "status": status,
    "manual": True,
    "date": date
  }
  print button
  buttonsList.append(button)

result = db.buttons.insert_many(buttonsList)