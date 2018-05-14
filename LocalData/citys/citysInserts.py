# -*- coding:utf-8 -*-  
"""
    Author:Zzh
    Github:HLoveMe
"""
import json,os
path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"citys.json")
from Apps.Address.models import Country,Province,City,Town,Village

def loadCitysAndInserts():

    with open(path, "rb") as file:
        data = json.load(file)
        print(data)
    pass

if __name__ == "__main__":
    print(loadCitysAndInserts())
    pass

