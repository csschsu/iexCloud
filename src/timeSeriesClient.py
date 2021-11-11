#!/usr/bin/python3
from common import iexDate, config
from common.common import resolveQueryParams, writeresultfile, checkresultfile
import requests
import datetime

env = config.Environment ()
action = "STOCK"


for symbol in env.symbols :
    if checkresultfile(action, symbol, iexDate.previousworkday()) :
        continue
    uri = env.iexBase + "/stock/<INSERT_SYMBOL>/chart/date/<INSERT_DATE>" + env.token
    uri = resolveQueryParams(uri, symbol, iexDate.previousworkday())
    print ("Query uri :" + uri )
    r = requests.get(uri)
    writeresultfile(r.text, action, symbol, iexDate.previousworkday())

print( datetime.datetime.now().strftime("%G-%m-%d %H:%M:%S")+ " END Client")