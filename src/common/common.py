import json
import os


def resolveQueryParams ( query : str, symbol : str, date:str ) :
    query = query.replace( "<INSERT_SYMBOL>", symbol)
    query = query.replace( "<INSERT_DATE>", date)
    return query

def writeresultfile ( data :str, symbol :str, date : str ):
    res_json = json.loads(data)
    with open(resultfilename( symbol, date), 'w') as f:
        s = json.dumps(res_json, indent=2)
        f.write('%s\n' % (s))
        f.close()
def resultfilename (symbol :str, date : str) :
    return "../data/" + symbol + "_" + date + ".dat"

def checkresultfile ( symbol :str, date : str ):
    return os.path.isfile(resultfilename( symbol, date))