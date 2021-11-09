#!/usr/bin/python3
import requests
import json
import iexDate
import config

def resolveQueryParams ( query : str, symbol : str, date:str ) :
    query = query.replace( "<INSERT_SYMBOL>", symbol)
    query = query.replace( "<INSERT_DATE>", date)
    return query

def writeresultfile ( data :str ):
    res_json = json.loads(data)
    # print(json.dumps(res_json, indent=4, sort_keys=True))
    filename = symbol + "_" + iexDate.previousworkday() + ".dat"
    with open(filename, 'w') as f:
        s = json.dumps(res_json, indent=2)
        f.write('%s\n' % (s))
        f.close()
#
# MAIN
#

env = config.Environment ()

for symbol in env.symbols :
    uri = env.iexBase + "/stock/<INSERT_SYMBOL>/chart/date/<INSERT_DATE>" + env.token
    uri = resolveQueryParams(uri, symbol, iexDate.previousworkday())
    print ("Query uri :" + uri )
    r = requests.get(uri)
    writeresultfile(r.text)

print("END Client")
