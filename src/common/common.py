import json


def resolveQueryParams ( query : str, symbol : str, date:str ) :
    query = query.replace( "<INSERT_SYMBOL>", symbol)
    query = query.replace( "<INSERT_DATE>", date)
    return query

def writeresultfile ( data :str, symbol :str, date : str ):
    res_json = json.loads(data)
    # print(json.dumps(res_json, indent=4, sort_keys=True))
    filename = symbol + "_" + date + ".dat"
    with open(filename, 'w') as f:
        s = json.dumps(res_json, indent=2)
        f.write('%s\n' % (s))
        f.close()

