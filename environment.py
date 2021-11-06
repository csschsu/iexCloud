def gettoken (file) :
    f = open( file , "r" )
    token = f.read()
    token = token.replace( "\n", "")
    return token

class Environment:
    # querystring 'https://sandbox.iexapis.com/stable/time-series?token=<token>'
    def __init__(self, target : str, querystring: str):
        if target.lower() == "p" :
            self.iexBase = "https://cloud.iexapis.com/stable"
        else :
            self.iexBase = "https://sandbox.iexapis.com/stable"
        self.token =  "?token=" + gettoken("/home/christer/iextoken_sandbox.dat")
        self.query =  self.iexBase + querystring + self.token


