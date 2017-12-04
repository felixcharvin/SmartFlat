import datetime
import pymongo
from pymongo import MongoClient
import sys
import os

client = MongoClient('mongodb://dreamteam:domotique@ds133311.mlab.com:33311/smartflat')
db = client.smartflat

PIN_LR = 9
PIN_TV = 11
PIN_K = 6
PATH = os.path.dirname(os.path.realpath(__file__))

TYPE = sys.argv[1]
ACTION = sys.argv[2]
MANUAL = int(sys.argv[3]) if len(sys.argv)>3 else 0

print "BTN_MANAGER : { type: "+TYPE+", status: "+str(STATUS)+", manual: "+str(MANUAL)+" }"

if TYPE in "alarm" and ACTION in "alert":
    os.system("python "+PATH+"/led_switch.py "+PIN_LR+" 1 "+str(MANUAL))
    os.system("python "+PATH+"/led_switch.py "+PIN_K+" 1 "+str(MANUAL))
    os.system("python "+PATH+"/led_switch.py "+PIN_TV+" 1 "+str(MANUAL))
elif TYPE in "luminosity":
  print "todo: luminosity event"
elif TYPE in "thermometer":
  print "todo: thermometer event"