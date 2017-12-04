import os
import sys
import signal
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')
db = client.smartflat

ID = ObjectId(sys.argv[1])

pid = db.sensors.find_one({"_id": ID})["pid"]
db.sensors.update_one({"_id": ID}, {"$set":{"status": "off"}})

os.kill(pid, signal.SIGTERM) #or signal.SIGKILL 
