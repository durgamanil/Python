# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 21:37:24 2019

@author: Onyx1
"""

l=[10,20,30,40,10,20,10,10]
target=int(input("enter the value to search"))
try:
    print(target,"available and its first occurence is at:",l.index(target))
except ValueError:
    print(target,"not available")

