#!/usr/bin/python3
from common import iexDate, config
from common.common import resolveQueryParams, writeresultfile
import requests

env = config.Environment ()

for symbol in env.symbols :
    uri = env.iexBase + "/stock/<INSERT_SYMBOL>/chart/date/<INSERT_DATE>" + env.token
    uri = resolveQueryParams(uri, symbol, iexDate.previousworkday())
    print ("Query uri :" + uri )
    r = requests.get(uri)
    writeresultfile(r.text, symbol, iexDate.previousworkday())

print("END Client")
