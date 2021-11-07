import environment as env
import requests
import json
import iexDate

def resolveQueryParams ( query : str, symbol : str, date:str ) :
    query = query.replace( "<INSERT_SYMBOL>", symbol)
    query = query.replace( "<INSERT_DATE>", date)
    return query


env = env.Environment ( "/stock/<INSERT_SYMBOL>/chart/date/<INSERT_DATE>")
query = resolveQueryParams(env.query, "AAPL", iexDate.previousworkday())

#r = requests.get(env.query)
#res_json = json.loads(r.text)
#print(json.dumps(res_json, indent=4, sort_keys=True))
print("END Client")