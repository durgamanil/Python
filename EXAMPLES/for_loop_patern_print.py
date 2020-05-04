# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 12:24:52 2020

@author: Onyx1
"""

n=int(input("Enter number of rows:"))
for i in range (1,n+1):
    print(" "*(n-i),end="")
    print("*"*i)
    