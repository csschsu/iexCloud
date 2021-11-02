import requests
import json

def gettoken (file) :
    f = open( file , "r" )
    token = f.read()
    token = token.replace( "\n", "")
    return token

uri = 'https://sandbox.iexapis.com/stable/time-series/REPORTED_FINANCIALS/IBM?token=<token>'
uri = uri.replace('<token>',gettoken("/home/christer/iextoken_sandbox.dat"))
r = requests.get(uri)
res_json = json.loads(r.text)
print(json.dumps(res_json, indent=4, sort_keys=True))
print(res_json)
print("END")