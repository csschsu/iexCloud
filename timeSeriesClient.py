import environment as env
import requests
import json

env = env.Environment ( "s", "/stock/AAPL/chart/date/20211015")
#https://cloud.iexapis.com/stable/stock/INSERT_SYMBOL/chart/date/INSERT_DATE?token=INSERT_TOKEN

print (env.query)
r = requests.get(env.query)
res_json = json.loads(r.text)
print(json.dumps(res_json, indent=4, sort_keys=True))
print("END Client")