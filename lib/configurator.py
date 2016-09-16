import json, os

filename = os.path.join(os.path.dirname(__file__), '../config.json')
with open(filename) as f:  
    data = json.load(f)

def getList(key, default):
    if key in data and type(data[key]) is list:
        return data[key]
    else:
        return default

def getDict(key, default):
    if key in data and type(data[key]) is dict:
        return data[key]
    else:
        return default

def getString(key, default):
    if key in data and type(data[key]) is str:
        return data[key]
    else:
        return default

def getJson():
    return data
