#!/usr/bin/python3
from common import iexDate, config
from common.common import resolveQueryParams, writeresultfile, checkresultfile
import requests
import datetime

env = config.Environment ()
action = "STATS"
sdat = iexDate.today()

for symbol in env.symbols :
    if checkresultfile( action, symbol, sdat) :
        continue
    uri = env.iexBase + "/stock/<INSERT_SYMBOL>/stats" + env.token
    uri = resolveQueryParams(uri, symbol, iexDate.previousworkday())
    print ("Query uri :" + uri )
    r = requests.get(uri)
    writeresultfile(r.text, action, symbol, sdat)

print( datetime.datetime.now().strftime("%G-%m-%d %H:%M:%S")+ " END Client")