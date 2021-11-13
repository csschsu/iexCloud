#!/usr/bin/python3
from common import iexDate
from common import iexCloudConfig as conf
from common.common import resolveQueryParams, writeresultfile, checkresultfile
import requests
import datetime

action = "STOCK"
sdat = iexDate.previousworkday()
symbols = conf.get("symbols").split(",")

for symbol in symbols :
    if checkresultfile(action, symbol, sdat) :
        continue
    uri = conf.get("iexBase") + "/stock/<INSERT_SYMBOL>/chart/date/<INSERT_DATE>" + conf.get("token")
    uri = resolveQueryParams(uri, symbol, iexDate.previousworkday())
    print ("Query uri :" + uri )
    r = requests.get(uri)
    writeresultfile(r.text, action, symbol, sdat)

print( datetime.datetime.now().strftime("%G-%m-%d %H:%M:%S")+ " END Client")