import json
import os
import common.iexCloudConfig as iex

class InvalidAction(Exception):
    pass

def resolveQueryParams ( query : str, symbol : str, date:str ) :
    query = query.replace( "<INSERT_SYMBOL>", symbol)
    query = query.replace( "<INSERT_DATE>", date)
    return query

def writeresultfile ( data :str, action : str , symbol :str, date : str ):
        checkaction(action)
        res_json = json.loads(data)
        with open(resultfilename( action, symbol, date), 'w') as f:
            s = json.dumps(res_json, indent=2)
            f.write('%s\n' % (s))
            f.close()

def resultfilename (action : str, symbol :str, date : str) :
    filedeploypath = iex.get("filedeploypath")
    return filedeploypath + "/" + symbol + "_"  + action + "_" + date + ".json"

def checkresultfile ( action : str, symbol :str, date : str ):
    checkaction(action)
    return os.path.isfile(resultfilename( action ,symbol, date))

def checkaction ( action : str ) :
    allowed = ["STOCK", "STATS"]
    if action not in allowed :
        raise InvalidAction('Invalid action ' + action + " allowed : " + " ".join(allowed))
