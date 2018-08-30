#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' config '

__author__ = 'YaMaoDaXain'

import json

class config:
    def __init__(self):
        self.url = None
        self.outputFile = None        

def DictToConfig(obj):
    cg = None
    try:
        tempCg = config()
        tempCg.url = obj["url"]
        tempCg.outputFile = obj["outputFile"]

        cg = tempCg
    except:
        pass        
    return cg

def LoadFrJSON(file):
    obj = None
    try:
        with open(file, "r") as f:
            obj = json.load(f)
        obj = DictToConfig(obj)
    except:
        pass
    return obj

def UnitTest():
    ssss = LoadFrJSON('config.json')
    print(ssss)

if __name__ == '__main__':
    UnitTest()