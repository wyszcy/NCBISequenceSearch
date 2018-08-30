#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' define the class 'SearchSequence' '''

__author__ = 'YaMaoDaXain'

class SearchSequence:
    def __init__(self, seq, url, outputFile):
        self.__seq = seq
        self.__url = url
        self.__outputFile = outputFile
        self.__result = None
    
    @property
    def result(self):
        return self.__result
