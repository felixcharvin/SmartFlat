import datetime
import pymongo
from pymongo import MongoClient
import sys
import os

PIN_LR = 9
PIN_TV = 11
PIN_K = 6
PIN_WIN = 2
PIN_FUR = 13
PATH = os.path.dirname(os.path.realpath(__file__))

ACTION = sys.argv[1]
MANUAL = int(sys.argv[3]) if len(sys.argv)>3 else 0

print "ALARM_MANAGER : { action: "+ACTION+", manual: "+str(MANUAL)+" }"

if ACTION in "alert":
  os.system("python "+PATH+"/led_switch.py "+str(PIN_LR)+" 1 "+str(MANUAL))
  os.system("python "+PATH+"/led_switch.py "+str(PIN_K)+" 1 "+str(MANUAL))
  os.system("python "+PATH+"/led_switch.py "+str(PIN_TV)+" 1 "+str(MANUAL))
elif ACTION in "on":
  os.system("python "+PATH+"/led_switch.py "+str(PIN_LR)+" 0 "+str(MANUAL))
  os.system("python "+PATH+"/led_switch.py "+str(PIN_K)+" 0 "+str(MANUAL))
  os.system("python "+PATH+"/led_switch.py "+str(PIN_TV)+" 0 "+str(MANUAL))
  os.system("python "+PATH+"/led_switch.py "+str(PIN_WIN)+" 0 "+str(MANUAL))
  os.system("python "+PATH+"/led_switch.py "+str(PIN_FUR)+" 0 "+str(MANUAL))
