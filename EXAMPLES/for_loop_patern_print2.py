# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 12:56:48 2020

@author: Onyx1
"""
m=n=int(input("Enter number of rows:"))
for i in range(0, n):
    print(i)
    for j in range(0,m):
        print(end=" ")
    m = m - 1 
    for j in range(0, i + 1):
        print("* ", end=' ')
    print(" ")