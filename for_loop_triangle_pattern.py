# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 13:47:22 2020

@author: Onyx1
"""

k = 0
rows = int(input("enter number of rows:"))
for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
    while k != (2*i-1):
        print("* ", end="")
        k = k + 1
    k = 0
    print()