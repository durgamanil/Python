# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 22:28:30 2020

@author: Onyx1
"""
import pymysql
conn=pymysql.connect(host="localhost",user="root",password="",db="sslabs")
mycursor=conn.cursor()

def ShowTableFromDB():
    mycursor.execute("SELECT * FROM users")
    row = mycursor.fetchone()
    while row is not None:
        print(row)
        row = mycursor.fetchone()
    

def InsertIntoTable():
    name=input("enter name")
    age=int(input("enter age"))
    #mycursor.execute("INSERT INTO `users`(`id`, `name`, `age`, `reg_date`) VALUES (null,'omkar','30',null);")
    mycursor.execute("INSERT INTO `users`(`id`, `name`, `age`, `reg_date`) VALUES (null,%s,%s,null);",(name,age))
    print("name:",name,"\nage:",age)
    conn.commit()