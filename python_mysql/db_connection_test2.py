# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 14:42:07 2020

@author: Onyx1
"""

#!/usr/bin/python

import mysql.connector

# Open database connection
db = mysql.connector.connect("localhost","test","test123","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Database version : %s " % data)

# disconnect from server
db.close()