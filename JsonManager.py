import json
import pandas as pd

def loadBeta(file_name:str, folder:str=None):
    return pd.Series(json.loads(open(f"{folder}/{file_name}", "r").read()))

def loadAlpha(file_name:str, folder:str=None):
    return pd.DataFrame(json.loads(open(f"{folder}/{file_name}", "r").read()))

def saveJson(dct:dict, title:str, folder:str =None):
    json.dump(dct, open(f"{folder}/{title}", "w"))