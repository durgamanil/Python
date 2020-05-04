# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 20:09:39 2020

@author: Onyx1
"""

import pymysql
from db_related_file import InsertIntoTable

conn=pymysql.connect(host="localhost",user="root",password="",db="sslabs")
mycursor=conn.cursor()

print("\nPlease enter your choice\n")
choice=int(input("1.add\n2.show\n\n"))


if choice==1:  
    InsertIntoTable()
elif choice ==2 :
    ShowTableFromDB()
    


#conn.commit()
conn.close()


