#!/usr/bin/python3
import os, sys

def gettoken(file):
    f = open(file, "r")
    token = f.read()
    token = token.replace("\n", "")
    return token

def getsymbols(file):
    symbols = []
    f = open(file, "r")
    while line := f.readline():
        symbols.append(line.rstrip())
    return symbols

class Environment:
    def __init__(self):
        file = sys.argv[0]
        pathname: str = os.path.dirname(file)
        # print('running from : ' + os.path.abspath(pathname))
        # print('file is : ' + file)
        s = pathname.split("/")
        if s[-1] == "test":   # run start in the test directory ( or else )
            self.iexBase = "https://sandbox.iexapis.com/stable"
            self.token = "?token=" + gettoken("/home/christer/iextoken_sandbox.dat")
            self.symbols = getsymbols("/home/christer/iextoken_sandbox_symbols.dat")
        else :
            self.iexBase = "https://cloud.iexapis.com/stable"
            self.token = "?token=" + gettoken("/usr/local/iexCloud/iextoken_prod.dat")
            self.symbols = getsymbols("/home/christer/iextoken_prod_symbols.dat")
