#!/usr/bin/python3
import os,sys

def gettoken (file) :
    f = open( file , "r" )
    token = f.read()
    token = token.replace( "\n", "")
    return token

file = sys.argv[0]
pathname: str = os.path.dirname(file)
print ('running from : ' + os.path.abspath(pathname))
print ('file is : ' + file )
s = pathname.split("/")
if s[-1] == "test" :
    #self.iexBase = "https://sandbox.iexapis.com/stable"
    #self.token =  "?token=" + gettoken("/home/christer/iextoken_sandbox.dat")
    print ( "https://sandbox.iexapis.com/stable" + "?token=" + gettoken("/home/christer/iextoken_sandbox.dat"))
