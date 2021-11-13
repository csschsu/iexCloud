import json

def get ( key : str ) :
    with open('config.json', "r") as jsonfile:
        data = json.load(jsonfile) # Reading the file
        jsonfile.close()
    return (data[key])
