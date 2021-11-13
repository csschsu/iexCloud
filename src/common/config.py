#!/usr/bin/python3
import json

class Config:
    def __init__(self):
        with open("config.json") as json_data_file:
            data = json.load(json_data_file)
            self.iexBase = data["iexBase"]
            self.token = data["token"]
            self.symbols = data["symbols"].split(",")
            self.filedeploypath = data["filedeploypath"]
