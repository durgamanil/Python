# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 07:52:53 2020

@author: Onyx1
"""

class Student:
    def __init__(self,x,y,z):
        self.name=x
        self.rollno=y
        self.marks=z
    def display(self):
        print("name:",self.name)
        print("rollno:",self.rollno)
        print("marks:",self.marks)
   
        
s=Student("anil",100,90)
s.display()


