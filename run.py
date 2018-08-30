#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' main '

__author__ = 'YaMaoDaXain'

import sys
import json

from NCBISequenceSearch import SearchSequence
import config

def Run():
    cg = config.LoadFrJSON('.\\config.json')
    if not cg:
        print(r'can not find the config file')
        return -2
    # if len(sys.argv) < 2:
    #     print('please input the sequence after the application')
    #     return -1
    # seqFile = sys.argv[1]
    # seq = LoadSeq(seqFile)
    seq = LoadSeq(r'.\seq.txt')
    searcher = SearchSequence(seq=seq, url=cg.url, outputFile=cg.outputFile)    

def LoadSeq(file):
    seq = None
    with open(file, "r") as f:
        seq = f.read()
    return seq

if __name__ == '__main__':
    Run()